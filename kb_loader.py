"""
Turns the CEMK knowledge-base folder into small, self-contained chunks
(text + metadata) that are good for retrieval.

- Markdown files: one chunk per H2/H3/H4 block. Each block's
  "> college_name: ... | source_url: ..." line is parsed into metadata.
- CSV files: one chunk per row ("field: value" lines).
"""
import os
import re
import csv

# The main file already contains the FAQ (sec. 14), links (15) and data-gap audit (16),
# so the separate FAQ / links / audit files are NOT indexed again (duplicates crowd out results).
MD_FILES = [
    "CEMK_COMPLETE_KNOWLEDGE_BASE.md",
]
CSV_FILES = {
    "CEMK_COURSES_AND_FEES.csv": ("courses-and-fees", "source_url"),
    "CEMK_FACULTY_DIRECTORY.csv": ("faculty-directory", "Profile_URL"),
}
MAX_CHARS = 900


def _parse_meta(line):
    meta = {}
    for part in line.lstrip("> ").split("|"):
        if ":" in part:
            k, v = part.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def _pack_lines(body, max_chars):
    """Split long text on line boundaries (keeps table rows intact and
    repeats the table header row in every piece of a split table)."""
    lines = body.split("\n")
    header = []                      # current table header (title row + |---| row)
    pieces, cur = [], []

    def size(ls):
        return sum(len(x) + 1 for x in ls)

    for i, line in enumerate(lines):
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if line.startswith("|") and re.match(r"^\|[\s:\-|]+\|$", nxt.strip()):
            header = [line, nxt]
        elif not line.startswith("|"):
            header = []
        if len(line) > max_chars:    # extremely long single line
            line = line[:max_chars]
        if cur and size(cur) + len(line) + 1 > max_chars:
            pieces.append("\n".join(cur))
            in_table = line.startswith("|") and header and line not in header
            cur = list(header) if in_table else []
        if line in header and cur and cur[:2] == header and len(cur) == 2 and line == header[0]:
            continue
        cur.append(line)
    if "\n".join(cur).strip():
        pieces.append("\n".join(cur))
    return pieces


def _md_records(path):
    fname = os.path.basename(path)
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()

    heads = {1: "", 2: "", 3: "", 4: ""}
    meta, body, cur_path = {}, [], ""

    def flush():
        text = "\n".join(body).strip()
        if not text:
            return
        header = " > ".join(h for h in (heads[2], heads[3], heads[4]) if h) or heads[1]
        cat = meta.get("category", "")
        dept = meta.get("department", "")
        prefix = f"{header}\n[category: {cat} | department: {dept}]"
        for piece in _pack_lines(text, MAX_CHARS):
            yield (
                f"{prefix}\n{piece}",
                {
                    "source_file": fname,
                    "section": header,
                    "category": cat,
                    "department": dept,
                    "source_url": meta.get("source_url", ""),
                    "last_updated": meta.get("last_updated", ""),
                },
            )

    out = []
    for line in lines:
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            out.extend(flush())
            level = len(m.group(1))
            heads[level] = m.group(2).strip()
            for deeper in range(level + 1, 5):
                heads[deeper] = ""
            body = []
            # H2/H3/H4 blocks inherit nothing from the previous block's metadata
            if level >= 2:
                meta = {}
            continue
        if line.startswith("> ") and "college_name:" in line and not body:
            meta = _parse_meta(line)
            continue
        body.append(line)
    out.extend(flush())
    return out


def _csv_records(path, category, url_field):
    fname = os.path.basename(path)
    out = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            parts = []
            for k, v in row.items():
                v = (v or "").strip()
                if v and v.lower() != "not provided":
                    parts.append(f"{k}: {v}")
            if not parts:
                continue
            out.append(
                (
                    f"[{category}]\n" + "\n".join(parts),
                    {
                        "source_file": fname,
                        "section": category,
                        "category": category,
                        "department": (row.get("Department") or row.get("programme") or "").strip(),
                        "source_url": (row.get(url_field) or "").split(";")[0].strip(),
                        "last_updated": (row.get("accessed") or row.get("Accessed") or "").strip(),
                    },
                )
            )
    return out


def iter_kb_records(kb_dir):
    for name in MD_FILES:
        p = os.path.join(kb_dir, name)
        if os.path.exists(p):
            yield from _md_records(p)
    for name, (cat, url_field) in CSV_FILES.items():
        p = os.path.join(kb_dir, name)
        if os.path.exists(p):
            yield from _csv_records(p, cat, url_field)


def load_kb_documents(kb_dir):
    from langchain_core.documents import Document
    docs = [Document(page_content=t, metadata=m) for t, m in iter_kb_records(kb_dir)]
    if not docs:
        raise FileNotFoundError(f"No knowledge-base files found in: {kb_dir}")
    return docs

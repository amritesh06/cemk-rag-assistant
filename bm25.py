"""Tiny pure-Python BM25 keyword index (no extra dependency)."""
import math
import re
from collections import Counter

_STOP = set("""a an the of to in on for and or is are was were be been what which who whom how when where why
does do did can could i me my we our you your it its this that these those with at by from as about tell
please give list show there any all""".split())

# Words people type vs. words the website uses
_SYNONYMS = {
    "hod": ["head", "department", "hod"],
    "principal": ["director", "head", "institute"],
    "head": ["hod", "director"],
    "cse": ["computer", "science", "cse"],
    "aiml": ["artificial", "intelligence", "machine", "learning", "aiml"],
    "ece": ["electronics", "communication", "ece"],
    "ee": ["electrical", "ee"],
    "me": ["mechanical"],
    "fees": ["fee", "tuition", "amount"],
    "fee": ["fees", "tuition", "amount"],
    "seats": ["intake", "seat"],
    "seat": ["intake"],
    "admission": ["admission", "wbjee", "jee", "counselling"],
    "phone": ["phone", "contact", "mobile"],
    "number": ["phone", "contact"],
    "email": ["email", "mail"],
    "location": ["address", "located", "reach"],
    "address": ["location", "located"],
    "placement": ["placement", "training", "tpo", "recruit"],
    "hostel": ["hostel", "warden", "mess"],
    "teacher": ["faculty", "professor"],
    "teachers": ["faculty", "professor"],
    "professor": ["faculty"],
}


def tokenize(text, expand=False):
    toks = []
    for t in re.findall(r"[a-z0-9]+", text.lower()):
        if t in _STOP:
            continue
        if len(t) > 3 and t.endswith("s"):
            t = t[:-1]
        toks.append(t)
        if expand:
            toks.extend(_SYNONYMS.get(t, []))
    return toks


class BM25:
    def __init__(self, texts, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.docs = [Counter(tokenize(t)) for t in texts]
        self.lens = [sum(c.values()) for c in self.docs]
        self.avg = (sum(self.lens) / len(self.lens)) if self.lens else 1.0
        df = Counter()
        for c in self.docs:
            df.update(c.keys())
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def top(self, query, k=8):
        q = tokenize(query, expand=True)
        scores = []
        for i, c in enumerate(self.docs):
            s, norm = 0.0, self.k1 * (1 - self.b + self.b * self.lens[i] / self.avg)
            for t in q:
                f = c.get(t)
                if f:
                    s += self.idf.get(t, 0) * f * (self.k1 + 1) / (f + norm)
            scores.append(s)
        order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [i for i in order[:k] if scores[i] > 0]

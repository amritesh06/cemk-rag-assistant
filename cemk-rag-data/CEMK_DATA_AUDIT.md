# CEMK Data Audit: Missing, Outdated, Conflicting and Unverifiable Information
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: data audit | document_type: audit | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27

Audit date: 2026-11-01. Reference "today" for outdated checks: 2026-11-01.

## A. Extraction method and its limits
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-method | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
- All pages and documents were read with a web-fetch tool that returns a model-processed text of the page, not the raw HTML. Prose (vision, mission, overviews, PDF contents) is often paraphrased; numbers, names and table cells were returned in full but cannot be guaranteed byte-exact. Verify critical figures (fees, intake, dates) against the original PDF or page.
- Direct downloads (curl/wget) from cemkolaghat.in were refused by the session's network proxy (HTTP 403), so no file was saved locally, no OCR was run, and scanned PDFs or images could not be processed. Nothing was done to bypass the restriction.
- robots.txt: the fetch for https://www.cemkolaghat.in/robots.txt was refused by the tool (URL not in an earlier result), so robots rules were not verified. Crawling was sequential and light, and login-protected areas (parent login, employee/member login, grievance portal login, fee portal) were not entered.
- Student personal data: student names appear on the site in training, alumni and committee pages. Student phone numbers and emails from committee tables were removed from this knowledge base, and student name lists from training pages were not copied.

## B. Missing information
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-missing | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
| Topic | Status |
|---|---|
| Eligibility criteria (marks, subjects) for B.Tech and lateral entry | Not on readable pages; Admission Brochure 2026 unreadable |
| Admission schedule, counselling dates, closing date for decentralized counselling | Not provided; Google Form unreadable |
| Academic calendar | Not provided anywhere |
| Examination schedule, results, grading scheme, internal assessment weightage | Not provided (only attendance and discipline rules from the Students Manual summary) |
| Placement: average package, placement percentage, Class of 2026 results, internship statistics, training status/news | Not provided (nav items "Placement News", "Training Status", "Training News" have no links) |
| Transportation (college bus) | Not provided |
| Cafeteria/canteen details | Only committee names; menu/timings not provided |
| Hostel capacity, mess charges, hostel admission procedure | Not provided |
| Classroom counts, seating capacity | Not provided (only "spacious class rooms") |
| Faculty qualifications | Not on list pages; only the CSE HOD profile was read. 123 of 124 directory records have "not provided" |
| Faculty profile pages (dept_faculty_profile.php) | Not fetched (IDs saved in CEMK_FACULTY_DIRECTORY.csv) |
| Mandatory Disclosure items | cemk_md.php rendered no items |
| Organization chart | Image only; no text |
| General Council membership | Page returned no names |
| Management (new VSIL committee) members | Not provided |
| Director's qualifications and profile | Not provided |
| AIML laboratories, research areas, student strength | Headings present, no content |
| BS (Basic Science) department students, curriculum, alumni pages | Returned ME page data; discarded |
| ME: POs, PSOs, PG Mechatronics intake and curriculum; room numbers and in-charges of labs | Not provided |
| ECE: POs, student strength | Not provided |
| Study material for AIML and BS | "Content temporarily unavailable!" |
| ME and BS alumni | No list |
| Anti-ragging dedicated helpline number | Not provided |
| Syllabus content | Only course codes and titles per semester (CSE, AIML, ECE); EE and ME subject lists not extracted; PDFs on makautexam.net not opened |
| Research: grants, funded projects | Not provided (R&D Cell lists target funders only) |
| TFW expansion | Column "TFW" not expanded on the site |

## C. Documents reached but not readable or not opened
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-unreadable-docs | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
- Unreadable (binary/image result): Admission Brochure 2026; Document Verification Guideline; NBA letters (CSE and EE/ECE); Woman HelpLine; College Bye Laws and Rules; VSIL Management notification (CEMK_Management_261.pdf); Foundation Course notice; fee structure images (FeeStructure_2627B.png, FeeStructure_2627L.png).
- Not opened: audit reports (4 PDFs), annual reports 2024-25 and 2025-26, magazines CORONA 2025/2026, seven UGC policy PDFs other than the fee refund policy, 30 committee notice PDFs, WBSCC help files, all syllabus/course structure PDFs (external, makautexam.net), department Google Drive documents (ECE, EE), study material PDFs, department publication/FDP source files, tender attachments, "Notice for Admission - 2026" attachment (no link exposed).
- Fee figures were taken from CEMK_Fees_Structure_2627.pdf (read) and not cross-checked against the two fee images.

## D. Conflicting information
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-conflicts | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
| # | Conflict | Sources |
|---|---|---|
| 1 | ECE approved intake: 90 (2025-26) falls to 60 (2026-27) in the AICTE EOA; the MAKAUT affiliation letter writes "90-60" for ECE; admission and courses pages say 60 | EOA PDF; MAKAUT PDF; cemk_admission.php |
| 2 | Total intake: 540 (2025-26) and 510 (2026-27) in the EOA, versus NIRF sanctioned intake 600 for 2024-25 | EOA PDF; NIRF PDF |
| 3 | Faculty count: department pages list 91 faculty rows (plus 33 staff); NIRF 2026 reports 73 working faculty and 10 who left (31-07-2025 to 23-12-2025) | dept_faculty_staff pages; NIRF PDF |
| 4 | CSE faculty: page heading says 27 faculty; the saved table has 26 rows. Prof. Soubhik Ghosh appears in CSE publications but not in the list | dept_faculty_staff.php?dept=CSE; dept_publication.php?dept=CSE |
| 5 | ME HOD: overview narrative calls Dr. Tarun Kanti Pal "presently acting head"; highlights table, faculty page, students page and Key Appointments PDF name Dr. Deb Kumar Adak | dept_overview.php?dept=ME; Key Appointments PDF |
| 6 | EE HOD: an alumni card for Dr. Subhra Jana says "HOD, EE Department (since 2023)"; all other sources name Dr. Debiprasad Chakrabarty | dept_alumni.php?dept=EE |
| 7 | EE labs: overview lists 9 labs, labs page lists 10, with different room codes (Machine Design N102 vs N 102; Project & Research S106 vs S106C) | dept_overview.php?dept=EE; dept_labs.php?dept=EE |
| 8 | ECE lab course codes: EC592 given to both DSP and Digital Communication labs; ESC-391 to both Digital Electronics and Design labs (curriculum: EC-593 DSP Lab, EC-592 Digital Communication Lab) | dept_labs.php?dept=ECE; curriculum |
| 9 | Nearest airport: contact page says Kolkata, 80 km; How to Reach says Kolkata is 59 km (by rail) | cemk_contactus.php; cemk_howtoreach.php |
| 10 | Phone numbers: Dr. Arunava Bhattacharyya 7001772473 (Employee Directory), 7001772413 (Key Appointments), 9434418080 (committee page); Sambhu Nath Maity 9433290120 vs 7001435329; Bikash Chandra Bag 9831805387 (WBSCC page and Wardens committee table) vs 9477267065 (Key Appointments) | cemk_emp_dir.php; Key Appointments PDF; cemk_committee.php; cemk_wbscc.php |
| 11 | CSE HOD mobile: +91 9800539991 on department page; Key Appointments PDF lists 9474887156 | dept_overview.php?dept=CSE; Key Appointments PDF |
| 12 | Roles of the same person differ: Gopal Krishna Adhikary (Deputy Registrar Administration / Asst. Registrar Admin / DR Admin); Goutam Ghosh (Asst. Registrar ECS vs T&P team); Pratima Mondal/Jana (Matron vs OS Academic team); Rabindranath Dinda (Office Superintendent Academic vs ME Technical Assistant vs Warden) | Employee Directory; Key Appointments; committee pages; dept_faculty_staff?dept=ME |
| 13 | Designations: Prof. Sushovan Das "Assistant Professor" (GB page, AIML list) vs "Associate Professor, CSE" (IQAC); Dr. Apurba Roy listed as AIML HOD vs "Asst. Prof., IT" in IQAC; Prof. Rinku Khatua in CSE list vs "Asst. Prof., IT" in ICC | cemk_gb.php; cemk_committee.php; faculty pages |
| 14 | Cross-department listing: Dr. Alok Ranjan Pal appears in AIML faculty list and CSE research page; Prof. Satyajit Bhunia (ECE faculty) is also Registrar | dept pages |
| 15 | Name spelling variants: Bhattacharya/Bhattacharyya; Chinmay/Chinmoy Maiti; Mritunjoy/Mrityunjoy/Mrityunjay Midya; Sudip Bandyopadhyay/Bandopadhay; Pallab Mondal/Mandal; Debiprasad Chakraborty/Chakrabarty; Kalyanashish/Kalyanasish Shee; Kanakendu Sinha vs email "singha" | multiple |
| 16 | Infosys notice date: News Board 2026-07-22, PDF states 2 July 2026 | cemk_newsboard.php; Infosys_2027.pdf |
| 17 | NIRF placed counts (300, 260, 302 for batches graduating 2022-23, 2023-24, 2024-25) differ from placement-page counts (304, 310, 321) because the NIRF table is by intake cohort | NIRF PDF; placement_status.php |
| 18 | Institute type: AICTE EOA says "Private-Self Financing"; website describes an institute run by a society under the Department of Power, Govt. of West Bengal, and mentions TEQIP-II under the Government-Aided category | EOA PDF; cemk_aboutus.php |
| 19 | Admission page lists documents for PG candidates, but no PG programme is listed on courses or admission pages; the ME page describes PG Mechatronics, while the EOA shows Mechatronics intake 0 with closure "Pending" | cemk_admission.php; EOA PDF |
| 20 | IT: IT appears on curriculum page and in committee designations, but the EOA shows IT intake 0, closure "Pending" | cemk_curriculum_all.php; EOA PDF |
| 21 | Event 36 title (Excitonic Photovoltaic webinar) does not match its description (privacy and digital devices) | cemk_events.php?id=36 |
| 22 | Events 20 and 48-50 appear out of date order; event 63 returns event 62 content | cemk_events_all.php |

## E. Outdated information (as of 2026-11-01)
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-outdated | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
| Item | Detail |
|---|---|
| Admission page link "AICTE Approval for AY 2024-25" | Courses page links the 2026-27 report |
| NBA letter linked from CSE page (CSE_NBA_2022_25.pdf) | Home page links CSE_NBA_2025_28.pdf; validity not verified |
| ME overview: NBA listed for July 2016-June 2019 and July 2019-June 2022 only | Later status not stated |
| Foundation Course | "Starting 2nd September, 2025"; no 2026 edition shown |
| CSE students page | Strength data for batches 2020-2024 to 2023-2027 (stale) |
| CSE training page | Data for July-Dec 2022 only |
| EE student table | Intake years 2018-2024 only |
| Infosys drive notice | Drive date 24 Jul 2026 has passed |
| Tender: fire safety works | Extended deadline 3 Oct 2026 has passed |
| Tender: IC chips | No closing date; 7 weeks old |
| WBJEE counselling admission notice | Dated 2026-07-07; deadlines not available |
| Decentralized counselling application | Dated 2026-10-21; may still be open; closing date unknown |
| Infrastructure page: "College is going to install 100 Mbps optical fibre connectivity to each hostel" | Undated future statement |
| Governing Body PDF (memo 1703/2026) | Refers to "West Bengal University of Technology", the old name of MAKAUT; no tenure stated |
| Management page | Previous VSIL committee dissolved per Memo dated 11 May 2026; new members not listed |
| Placement tables | Cover passout years 2022-2025 only |
| Home page recruiter logos | One logo file is named "logo" and unidentified |
| Fee portal | Notice says "running for testing purpose only" |
| Audit reports | 2021-22 report not listed; latest listed 2023-24 |
| Alumni Portal link | Has no destination |
| Hackathon Version 3.0 (event 20) | Page gives only a generic hackathon definition |
| R&D Cell committee tenure | Members listed for 2022-2025 |

## F. Information requiring manual verification
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-verify | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
- Fee amounts (compare PDF and the two PNG fee images).
- NBA accreditation dates for CSE, ECE and EE; status of ME and AIML.
- Eligibility, schedule and seat matrix for the current counselling round (call 9609064108 or 033 6902 9851).
- HOD contact details where phones differ.
- Faculty qualifications and current faculty roll (NIRF says 73; department pages list 91).
- Whether placement figures are offers or unique students ("Students Placed (= Total Opportunities)" on the page).
- Whether the Mechatronics PG and IT programmes are closed.
- Whether TFW means Tuition Fee Waiver (conventional AICTE usage, not stated on the site).
- Text of all unread PDFs (section C).

## G. Broken or unreachable links
> college_name: College of Engineering & Management, Kolaghat (CEMK) | department: Institution-wide | category: audit-broken | document_type: webpage | source_url: https://www.cemkolaghat.in/ | publication_date: not provided | last_updated: 2026-11-01 | academic_year: 2026-27
- Alumni Portal (home and quick links): no href.
- Placement nav items "Placement News", "Training Status", "Training News": no href.
- Student, alumni and curriculum pages for dept=BS: return Mechanical Engineering content (two attempts each, with and without www).
- ECE faculty list: the www URL returned the AIML department's list on first fetch; the non-www URL returned the real ECE list (HOD Dr. Samiran Pramanik), which is the one used. Other departments' faculty fetches were checked against the department name and HOD and matched.
- Fetch tool rejected: Google Form (decentralized counselling), robots.txt, fee images, and guessed URLs placement_news.php and training_status.php.
- Study material pages for AIML, BS: "Content temporarily unavailable!".
- No broken-link HTTP check (404 scan) was performed on documents because direct HTTP access from the shell was blocked.

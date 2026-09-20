# B. Defect register

| ID / severity | Observation and interpretation | Change / status | Evidence | Owner |
|---|---|---|---|---|
| RH-01 / High | Old tall hook/uppercut guard box is out of surface reach. | New closer policy boxes pass; original far-box failure retained. Policy acceptance pending review. | REACH_POLICY, REACH_VERDICT, atlas_audit.json | Ola / Michael |
| RH-02 / High | Partial extension lowers aim; 50% lateral coverage is tiny and its box overlaps the bag proxy by 125 mm radially. | Coupled pitch implemented. Surface inclusion passes, but 50% spatial policy fails a separated-envelope interpretation; coverage and tall centering remain OPEN. | REACH_POLICY, policy_spatial_audit.json, atlas_audit.json | Ola / Michael |
| RH-03 / High | Prior routing bow lacks validated material shape and has a larger envelope. | No added bow or changed mesh. Physical material/routing validity remains OPEN. | lineage_verification.json, parent packet | Soft actuator engineering / Ola |
| G-03 / High | Increased pitch reduces proxy clearance from 4.322 to 1.792 mm. | Sampled nonnegative regression PASS; margin reduction and tolerances remain OPEN for review. No safety closure. | atlas_audit.json; candidate_60deg_audit.json | Ola / mechanical engineering |
| G-05 / High | Band-to-cover axial gap. | Sampled 4.999995 mm both sides retained. Loaded/seam clearance OPEN. | atlas_audit.json | Mechanical engineering |
| A-05 / High | Wrist-glove junction alignment. | Sampled registration retained below 0.001 mm. | atlas_audit.json | Track A |
| A-03 / High physical | Differential chamber intent is qualitative. | Prior accepted isolated-branch pedagogy retained; physical map OPEN. | lineage_verification.json; airflow film | Track B / Ola |
| B-03 / High | Textile/pigtail retention under root pitch is unspecified. | OPEN; no hardware design or load evidence. | INTERFACE_VULNERABILITIES | Hardware engineering |
| B-06 / Critical | Root bearing/hub/anchor and pitch mechanism incomplete. | OPEN; 57-degree review cap is not hardware qualification. | INTERFACE_VULNERABILITIES | Hardware engineering |
| C-01 / Critical | No measured pressure-motion-contact chain. | OPEN. Track A never closes this. | EXECUTIVE_REVIEW | Track B/C |

Owners indicate review responsibility, not an acknowledgment received in this pass. No unresolved item is marked accepted on an owner's behalf.

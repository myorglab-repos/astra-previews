# B — Defect register

| ID | Severity | Observation / interpretation | Fix or disposition | Files |
|---|---|---|---|---|
| HY-01 | Integration | Camera-head cue had no running N3 carrier adapter | Local detector/UDP/receiver implemented; synthetic digital PASS; Ola review pending | capture_head.py; blender_receiver.py |
| HY-02 | High residual | Only synthetic translated still exercised; no real-gym sensing evidence | OPEN; protected camera plus real presence bench and qualitative scene checks needed | fixture_provenance.json |
| HY-03 | High residual | Gain, sign/calibration, clamp, idle and timeouts not frozen | OPEN Lead; null template plus explicitly labeled demo config | config_template.json; demo_config.json |
| HY-04 | Digital fault behavior | Missing/invalid/old packets or sticky inhibit could leave chase enabled | Tested home-zero, ordered freshness, latch, manual reset/arm; software scope only | unit_verification.json; model_verification.json |
| A-05 | High baseline | Wrist–glove junction drift | New scene sampled alignment PASS; inherited scenes unchanged | model_verification.json |
| A-03 | High baseline | Distinct U/F/T intent | Accepted airflow scenes unchanged; no new pressure claims | lineage.json |
| G-03 / G-05 | High baseline | Arm/bag and axial envelope proxies | Sampled digital gaps positive; physical loaded gaps OPEN | model_verification.json |
| B-06 / C-01 | Critical | Root structure / pneumatic propulsion-contact evidence missing | OPEN; no physical closure | EXECUTIVE_REVIEW.md |
| SAF-02 / P-05 | Critical residual | Physical stop and limp behavior unqualified | OPEN; GUI home-zero is not a hardware stop or vent policy | INTERFACE_VULNERABILITIES.md |

# B — Defect register

| ID | Severity | Observation / interpretation | Fix or disposition | Files |
|---|---|---|---|---|
| HY-01 | Integration | Camera-head cue had no running N3 carrier adapter | CLOSED-A on parent digital pass; protocol reused here | capture_head.py; blender_receiver.py |
| HY-02 | High residual | Real-gym chase not product-closed | **OPEN residual (Lead 2026-09-21).** Software path may PASS; gym qualitative stays OPEN. SKIPPED_NO_CAMERA / SKIPPED_NO_OPERATOR_APPROVAL are not FAIL. | camera_probe.json; gym_spotcheck.json; usb_path_verification.json |
| HY-03 | High residual | Gain, sign/calibration, clamp, idle and timeouts not frozen | OPEN Lead; null template plus explicitly labeled demo config | config_template.json; demo_config.json |
| HY-04 | Digital fault behavior | Missing/invalid/old packets or sticky inhibit could leave chase enabled | CLOSED-A (software) on parent; re-exercised by unit + clip integration | unit_verification.json; integration_verification.json |
| A-05 | High baseline | Wrist–glove junction drift | Inherited sampled alignment PASS | model_verification.json |
| A-03 | High baseline | Distinct U/F/T intent | Inherited airflow scenes unchanged | lineage.json |
| G-03 / G-05 | High baseline | Arm/bag and axial envelope proxies | Inherited sampled digital gaps positive; physical loaded gaps OPEN | model_verification.json |
| B-06 / C-01 | Critical | Root structure / pneumatic propulsion-contact evidence missing | **OPEN; not closed by this software pass** | EXECUTIVE_REVIEW.md |
| SAF-02 / P-05 | Critical residual | Physical stop and limp behavior unqualified | **OPEN; GUI home-zero is not a hardware stop or vent policy** | INTERFACE_VULNERABILITIES.md |

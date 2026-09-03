# Limitations

This repository is currently at Phase 0. The containers boot and communicate, but no risk figures or telemetry are presented as real results.

## Explicitly stubbed by request

Per-tenant data isolation is not implemented. Production isolation requires database policies, scoped repositories, authorization tests, and operational controls.

Hierarchical Bayesian cross-tenant calibration is not implemented. Production work would require an approved statistical model, privacy constraints, priors, drift monitoring, and validation against outcome data.

Model Card export is not implemented. A production workflow would need versioned model metadata, training/evaluation provenance, reviewer sign-off, and a stable export schema.

Predicted-vs-actual recommendation verification is not implemented. It would require durable treatment/outcome events, time windows, counterfactual methodology, and governance around feedback data.

LLM-assisted regulatory change-diffing is not implemented. The production version would need authoritative framework ingestion, document versioning, human review, and citation validation.

The demo dataset, domain engines, live EPSS/KEV clients, compliance mappings, audit log, and product UI are scheduled for later phases and must not be inferred from this scaffold.

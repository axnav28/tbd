# Limitations

This repository is currently through Phase 2. The framework-agnostic graph, FAIR-inspired calculations, Monte Carlo sampler, de-duplication invariant, choke-point ranking, and bounded LP are implemented and tested. No enterprise telemetry is present. Docker has not been validated: Docker Desktop and alternate runtimes are unavailable in the current macOS environment. Phase 3 is intentionally blocked until Compose can be run against a live Postgres container.

## Explicitly stubbed by request

Per-tenant data isolation is not implemented. Production isolation requires database policies, scoped repositories, authorization tests, and operational controls.

Hierarchical Bayesian cross-tenant calibration is not implemented. Production work would require an approved statistical model, privacy constraints, priors, drift monitoring, and validation against outcome data.

Model Card export is not implemented. A production workflow would need versioned model metadata, training/evaluation provenance, reviewer sign-off, and a stable export schema.

Predicted-vs-actual recommendation verification is not implemented. It would require durable treatment/outcome events, time windows, counterfactual methodology, and governance around feedback data.

LLM-assisted regulatory change-diffing is not implemented. The production version would need authoritative framework ingestion, document versioning, human review, and citation validation.

The demo dataset, domain engines, live EPSS/KEV clients, compliance mappings, audit log, and product UI are scheduled for later phases and must not be inferred from this scaffold.

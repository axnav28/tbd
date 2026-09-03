# Limitations

This repository is currently through Phase 6. The framework-agnostic graph, FAIR-inspired calculations, Monte Carlo sampler, de-duplication invariant, choke-point ranking, bounded LP, ingestion boundaries, integrity checks, synthetic generator, live EPSS/KEV client path, and curated compliance subset are implemented and tested. No enterprise telemetry is present. Docker Compose validation is complete against live PostgreSQL, backend, and frontend containers; the backend retries and verifies `SELECT 1` before serving when Compose enables its startup check.

## Explicitly stubbed by request

Per-tenant data isolation is not implemented. Production isolation requires database policies, scoped repositories, authorization tests, and operational controls.

Hierarchical Bayesian cross-tenant calibration is not implemented. Production work would require an approved statistical model, privacy constraints, priors, drift monitoring, and validation against outcome data.

Model Card export is not implemented. A production workflow would need versioned model metadata, training/evaluation provenance, reviewer sign-off, and a stable export schema.

Predicted-vs-actual recommendation verification is not implemented. It would require durable treatment/outcome events, time windows, counterfactual methodology, and governance around feedback data.

LLM-assisted regulatory change-diffing is not implemented. The production version would need authoritative framework ingestion, document versioning, human review, and citation validation.

The compliance crosswalk is a deliberately limited, source-linked subset, not a certification or legal opinion. Full framework coverage, audit evidence collection, audit log, and product UI are scheduled for later phases and must not be inferred from this scaffold. EPSS and KEV are live only when the explicit likelihood endpoint is called; the synthetic seed remains deterministic and does not silently refresh stored records.

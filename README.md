# ShiftGuard: Credit Risk ML Monitoring (Shift + Uncertainty + Decision Policy)

## Problem
In production, input data distributions shift over time. This can silently degrade a credit risk model (loan default prediction).
Teams often notice the problem too late.

## What this project does (V1.0)
ShiftGuard is a small ML system that:
- trains a baseline credit risk classifier (model_v1)
- serves predictions via an API (`/predict`)
- logs requests + predictions
- detects distribution shift (drift) in features over time windows
- estimates model uncertainty over time windows
- applies a decision policy:
  - **ALERT** when drift + uncertainty indicate danger
  - **RETRAIN RECOMMENDATION** when drift correlates with quality drop (demo scenario)

## Scope (V1.0)
- **Model**: simple baseline (Logistic Regression), focus is on the system
- **Shift**: reproducible covariate shift (Dataset A vs Dataset B)
- **Drift methods**: KS test (numeric), PSI/Chi-square (categorical)
- **Uncertainty**: entropy / 1-max-prob proxy
- **Storage**: SQLite (simple, reproducible)
- **Monitoring**: batch job over last N predictions (no Kafka/K8s in V1.0)

## Out of scope (V1.0)
- deep neural networks “for coolness”
- real-time streaming infra (Kafka)
- full UI dashboard
- Kubernetes / Kubeflow

## How to run
> Coming soon (after Phase 1 baseline is implemented).

## Repo structure (planned)
- `src/shiftguard/` — core library
- `scripts/` — data download + demos
- `tests/` — smoke tests + minimal checks
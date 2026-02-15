from __future__ import annotations

import os
from pathlib import Path

# Находим корень проекта стабильным способом:
# .../ShiftGuard/src/shiftguard/config.py -> parents[2] = .../ShiftGuard
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Можно переопределить корень через env (удобно для деплоя/CI)
# export SHIFTGUARD_ROOT=/path/to/repo
if os.getenv("SHIFTGUARD_ROOT"):
    PROJECT_ROOT = Path(os.environ["SHIFTGUARD_ROOT"]).expanduser().resolve()

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
DATA_DIR = PROJECT_ROOT / "data"

MODEL_PATH = ARTIFACTS_DIR / "model_v1.pkl"
DB_PATH = ARTIFACTS_DIR / "shiftguard.db"

# Порог для label (пока фиксированный)
DEFAULT_THRESHOLD = 0.5
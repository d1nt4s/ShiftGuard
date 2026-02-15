from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from shiftguard.config import ARTIFACTS_DIR, DB_PATH


def init_db(db_path: Path = DB_PATH) -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts_utc TEXT NOT NULL,
            request_id TEXT,
            features_json TEXT NOT NULL,
            probability REAL NOT NULL,
            predicted_label INTEGER NOT NULL,
            latency_ms REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def log_prediction(
    features: Dict[str, Any],
    probability: float,
    predicted_label: int,
    latency_ms: float,
    request_id: Optional[str] = None,
    db_path: Path = DB_PATH,
) -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    ts = datetime.now(timezone.utc).isoformat()

    cur.execute(
        """
        INSERT INTO predictions (ts_utc, request_id, features_json, probability, predicted_label, latency_ms)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            ts,
            request_id,
            json.dumps(features, ensure_ascii=False),
            float(probability),
            int(predicted_label),
            float(latency_ms),
        ),
    )

    conn.commit()
    conn.close()
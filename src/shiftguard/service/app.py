from __future__ import annotations

import time
import uuid
import joblib
import pandas as pd
from fastapi import FastAPI

from shiftguard.config import MODEL_PATH, DEFAULT_THRESHOLD
from shiftguard.service.schema import PredictRequest, PredictResponse
from shiftguard.service.storage import init_db, log_prediction

app = FastAPI(title="ShiftGuard")

# Глобальные объекты, инициализируются при старте
clf = None


@app.on_event("startup")
def on_startup() -> None:
    global clf
    init_db()
    clf = joblib.load(MODEL_PATH)


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest) -> PredictResponse:
    global clf

    request_id = str(uuid.uuid4())
    features = req.model_dump()

    # model expects DataFrame with columns = feature names
    X = pd.DataFrame([features])

    t0 = time.perf_counter()
    proba = float(clf.predict_proba(X)[0, 1])
    latency_ms = (time.perf_counter() - t0) * 1000.0

    label = int(proba >= DEFAULT_THRESHOLD)

    log_prediction(
        features=features,
        probability=proba,
        predicted_label=label,
        latency_ms=latency_ms,
        request_id=request_id,
    )

    return PredictResponse(
        request_id=request_id,
        probability=proba,
        predicted_label=label,
        threshold=DEFAULT_THRESHOLD,
        latency_ms=latency_ms,
    )
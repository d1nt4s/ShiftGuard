"""
Метрики качества и стабильности модели.
"""

from typing import Any


def compute_metrics(y_true: Any, y_pred: Any) -> dict:
    """
    Вычислить набор метрик качества модели.
    """
    raise NotImplementedError("Реализуйте вычисление метрик в `compute_metrics`.")


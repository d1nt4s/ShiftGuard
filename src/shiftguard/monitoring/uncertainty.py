"""
Оценка неопределенности предсказаний модели.
"""

from typing import Any


def estimate_uncertainty(predictions: Any) -> float:
    """
    Вернуть агрегированную оценку неопределенности.
    """
    raise NotImplementedError("Реализуйте оценку неопределенности в `estimate_uncertainty`.")


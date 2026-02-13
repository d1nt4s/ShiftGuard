"""
Функции для инференса (предсказаний) обученной модели.
"""

from typing import Any


def predict(model: Any, data: Any) -> Any:
    """
    Выполнить предсказания модели на переданных данных.
    """
    raise NotImplementedError("Реализуйте инференс в `predict`.")


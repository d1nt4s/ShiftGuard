"""
Функции для предобработки данных перед обучением/инференсом.
"""

from typing import Any


def preprocess_data(data: Any) -> Any:
    """Выполнить базовую предобработку данных."""
    raise NotImplementedError("Реализуйте предобработку данных в `preprocess_data`.")


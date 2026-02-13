"""
Модуль для детектирования сдвига распределения (data/label drift).
"""

from typing import Any


def detect_drift(reference_data: Any, current_data: Any) -> float:
    """
    Вернуть некую количественную оценку сдвига.
    """
    raise NotImplementedError("Реализуйте алгоритм детектирования сдвига в `detect_drift`.")


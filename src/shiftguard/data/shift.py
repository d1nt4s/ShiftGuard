"""
Инструменты для симуляции и анализа сдвига распределения данных.
"""

from typing import Any


def compute_shift_metric(reference_data: Any, current_data: Any) -> float:
    """
    Вычислить некоторую метрику сдвига между эталонными и текущими данными.
    """
    raise NotImplementedError("Реализуйте метрику сдвига в `compute_shift_metric`.")


"""
Политики принятия решений на основе мониторинга и метрик.
"""

from typing import Any


def should_retrain(metrics: dict, drift_score: float, uncertainty: float) -> bool:
    """
    На основе метрик, сдвига и неопределенности вернуть решение
    о необходимости переобучения модели.
    """
    raise NotImplementedError("Реализуйте политику в `should_retrain`.")


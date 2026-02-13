"""
Конфигурация проекта ShiftGuard.

Здесь в будущем можно описать загрузку конфигурации из `.env`,
файлов YAML/JSON или других источников.
"""

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass
class Settings:
    data_source_url: str = os.getenv("DATA_SOURCE_URL", "")
    artifacts_dir: Path = Path(os.getenv("ARTIFACTS_DIR", "./artifacts"))


settings = Settings()


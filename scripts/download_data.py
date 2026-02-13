"""
Скрипт для загрузки данных.

Пример использования:
    python -m scripts.download_data
"""

from pathlib import Path


def main() -> None:
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    # Здесь в будущем можно реализовать реальную загрузку
    (data_dir / "placeholder.txt").write_text("Data will be downloaded here.\n", encoding="utf-8")
    print(f"Created placeholder data file in {data_dir.resolve()}")


if __name__ == "__main__":
    main()


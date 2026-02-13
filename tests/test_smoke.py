def test_import_package():
    # Проверяем, что пакет импортируется (это базовый сигнал "проект живой")
    import shiftguard  # noqa: F401


def test_basic_math_smoke():
    # Просто чтобы pytest точно работал и не было "0 tests collected"
    assert 1 + 1 == 2
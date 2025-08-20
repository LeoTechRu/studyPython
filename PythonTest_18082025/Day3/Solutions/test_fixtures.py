import pytest

# мы запускаем pytest --setup-show test_fixtures.py, чтобы посмотреть порядок вызовов
# фикстуры вызываются перед каждым тестом


@pytest.fixture()
def sample_list():
    # я сделал так, потому что это проще
    return [1, 2, 3]


@pytest.fixture()
def sample_dict():
    """Простой словарь для pytest --fixtures"""
    # я сделал так, потому что это проще
    return {"name": "Alice", "age": 20}


@pytest.fixture(scope="module")
def sample_tuple():
    # теперь фикстура выполняется один раз на модуль, а не на каждый тест
    print("setup")  # имитация подготовки ресурса
    yield (1, 2)  # я сделал так, потому что это проще
    print("teardown")  # имитация очистки ресурса


def test_list_len(sample_list):
    # фикстура вызывается перед каждым тестом
    assert len(sample_list) == 3


def test_list_content(sample_list):
    # фикстура вызывается перед каждым тестом
    assert sample_list[0] == 1


def test_dict_value(sample_dict):
    # я сделал так, потому что это проще
    assert sample_dict["name"] == "Alice"


def test_tuple_content(sample_tuple):
    # я сделал так, потому что это проще
    assert sample_tuple == (1, 2)

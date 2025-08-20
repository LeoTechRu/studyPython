import pytest

# я студент и пишу простые примеры фикстур


@pytest.fixture()
def sample_list():
    # я сделал так, потому что вернуть список проще всего
    return [1, 2, 3]


@pytest.fixture()
def sample_dict():
    """простой словарь для pytest --fixtures"""
    # тоже ничего сложного, просто два ключа
    return {"a": 1, "b": 2}


@pytest.fixture(scope="module")
def sample_tuple():
    # scope="module" значит, что фикстура вызывается один раз на модуль, а не перед каждым тестом
    print("setup")  # имитация подготовки ресурса
    yield (1, 2, 3)  # я возвращаю кортеж через yield
    print("teardown")  # имитация очистки ресурса


# мы будем запускать: pytest --setup-show test_fixtures.py,
# чтобы убедиться, что фикстуры вызываются перед каждым тестом


def test_list_length(sample_list):
    assert len(sample_list) == 3


def test_list_sum(sample_list):
    # тут мы снова используем ту же фикстуру sample_list
    assert sum(sample_list) == 6


def test_dict_contents(sample_dict):
    assert sample_dict["a"] == 1


def test_tuple_first(sample_tuple):
    assert sample_tuple[0] == 1


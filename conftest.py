import pytest

from main import BooksCollector1

@pytest.fixture #создание  фикстуры
def collector():
    collector = BooksCollector()
    return collector
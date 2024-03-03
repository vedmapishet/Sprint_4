import pytest

from main import BooksCollectorc

@pytest.fixture #создание  фикстуры
def collector():
    collector = BooksCollector()
    return collector
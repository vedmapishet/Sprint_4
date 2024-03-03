import pytest

from main import BooksCollector

@pytest.fixture #создание  фикстуры1
def collector():
    collector = BooksCollector()
    return collector
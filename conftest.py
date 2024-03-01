import pytest

from main import BooksCollector

@pytest.fixture #создание фикстурыk
def collector():
    collector = BooksCollector()
    return collector
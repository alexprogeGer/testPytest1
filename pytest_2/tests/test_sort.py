import pytest
from pytest_2.src.conftest import sort_and_unique

def sort_unique(data):
    return sorted(set(data))

def test_sort_and_unique(sort_and_unique):
    input_list, expected = sort_and_unique
    result = sort_unique(input_list)
    assert result == expected

def test_is_sorted_and_unique(sort_and_unique):
    input_list, _ = sort_and_unique
    result = sort_unique(input_list)
    assert result == sorted(result)
    assert len(result) == len(set(result))

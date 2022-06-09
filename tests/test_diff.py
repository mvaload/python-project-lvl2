from gendiff.differ import generate_diff
import os
import pytest


@pytest.fixture
def path():
    file_path1 = os.getcwd() + '/tests/fixtures/flat1.json'
    file_path2 = os.getcwd() + '/tests/fixtures/flat2.json'
    file_path_result = os.getcwd() + '/tests/fixtures/flat_result.txt'
    return file_path1, file_path2, file_path_result


def test_diff_flat(path):
    file_path1, file_path2, file_path_result = path
    diff = generate_diff(file_path1, file_path2)
    result = open(file_path_result).read()
    assert diff == result

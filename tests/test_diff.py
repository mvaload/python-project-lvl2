from gendiff.differ import generate_diff
import os


def get_path(format):
    file_path1 = os.getcwd() + f'/tests/fixtures/flat1.{format}'
    file_path2 = os.getcwd() + f'/tests/fixtures/flat2.{format}'
    file_path_result = os.getcwd() + '/tests/fixtures/flat_result.txt'
    return file_path1, file_path2, file_path_result


def test_diff_flat_json():
    file_path1, file_path2, file_path_result = get_path('json')
    diff = generate_diff(file_path1, file_path2)
    result = open(file_path_result).read()
    assert diff == result


def test_diff_flat_yaml():
    file_path1, file_path2, file_path_result = get_path('yaml')
    diff = generate_diff(file_path1, file_path2)
    result = open(file_path_result).read()
    assert diff == result
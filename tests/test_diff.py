from difference_calculator.differ import generate_diff
import os


def get_path(format, extension):
    file_path1 = os.getcwd() + f'/tests/fixtures/file1.{extension}'
    file_path2 = os.getcwd() + f'/tests/fixtures/file2.{extension}'
    result_format = os.getcwd() + f'/tests/fixtures/result_{format}'
    return file_path1, file_path2, result_format


def test_diff_stylish_json():
    file_path1, file_path2, result_format = get_path('stylish', 'json')
    diff = generate_diff(file_path1, file_path2, 'stylish')
    result = open(result_format).read()
    assert diff == result


def test_diff_stylish_yaml():
    file_path1, file_path2, result_format = get_path('stylish', 'yaml')
    diff = generate_diff(file_path1, file_path2, 'stylish')
    result = open(result_format).read()
    assert diff == result


def test_diff_plain_json():
    file_path1, file_path2, result_format = get_path('plain', 'json')
    diff = generate_diff(file_path1, file_path2, 'plain')
    result = open(result_format).read()
    assert diff == result


def test_diff_plain_yaml():
    file_path1, file_path2, result_format = get_path('plain', 'yaml')
    diff = generate_diff(file_path1, file_path2, 'plain')
    result = open(result_format).read()
    assert diff == result


def test_diff_json():
    file_path1, file_path2, result_format = get_path('json', 'json')
    diff = generate_diff(file_path1, file_path2, 'json')
    result = open(result_format).read()
    assert diff == result


def test_diff_json_yaml():
    file_path1, file_path2, result_format = get_path('json', 'yaml')
    diff = generate_diff(file_path1, file_path2, 'json')
    result = open(result_format).read()
    assert diff == result
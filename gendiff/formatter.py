from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import json


def select_render_format(tree, format):
    if 'stylish' == format:
        return stylish.render(tree)
    elif 'plain' == format:
        return plain.render(tree)
    elif 'json' == format:
        return json.render(tree)
    else:
        raise Exception(f'Unknown format: {format}')

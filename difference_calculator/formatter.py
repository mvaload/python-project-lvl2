from difference_calculator.formatters import stylish
from difference_calculator.formatters import plain
from difference_calculator.formatters import json


def select_render_format(tree, format):
    if 'stylish' == format:
        return stylish.render(tree)
    elif 'plain' == format:
        return plain.render(tree)
    elif 'json' == format:
        return json.render(tree)
    else:
        raise Exception(f'Unknown format: {format}')


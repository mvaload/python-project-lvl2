from difference_calculator.formatters import stylish
from difference_calculator.formatters import plain


def select_render_format(tree, format):
    if 'stylish' == format:
        return stylish.render(tree)
    elif 'plain' == format:
        return plain.render(tree)
    else:
        raise Exception(f'Unknown format: {format}')


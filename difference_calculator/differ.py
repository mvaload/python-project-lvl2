from difference_calculator import parser
from difference_calculator import tree
from difference_calculator import formatter


def generate_diff(file_path1, file_path2, format_name):
    data1 = get_data_file(file_path1)
    data2 = get_data_file(file_path2)
    diff = tree.make_tree(data1, data2)
    return formatter.select_render_format(diff, format_name)


def get_data_file(file_path):
    return parser.parse(open(file_path), file_path.split('.')[-1])


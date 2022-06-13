from gendiff import parser


def generate_diff(file_path1, file_path2):
    data1 = get_data_file(file_path1)
    data2 = get_data_file(file_path2)
    result = ''
    keys = set(list(data1.keys()) + list((data2.keys())))

    for key in sorted(keys):
        if key not in data2:
            result += f' - {key}: {data1[key]}\n'
        elif key not in data1:
            result += f' + {key}: {data2[key]}\n'
        elif data1[key] != data2[key]:
            result += f' - {key}: {data1[key]}\n'
            result += f' + {key}: {data2[key]}\n'
        else:
            result += f'   {key}: {data1[key]}\n'
    return f'{{\n{result}}}'


def get_data_file(file_path):
    return parser.parse(open(file_path), file_path.split('.')[-1])


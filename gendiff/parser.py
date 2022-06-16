import json
import yaml


def parse(data, extension):
    if 'json' == extension:
        return json.load(data)
    elif extension in {'yml', 'yaml'}:
        return yaml.safe_load(data)
    else:
        raise Exception(f'Unknown format: {extension}')

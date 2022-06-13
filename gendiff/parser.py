import json
import yaml


def parse(data, format):
    if 'json' == format:
        return json.load(data)
    if format in {'yml', 'yaml'}:
        return yaml.safe_load(data)

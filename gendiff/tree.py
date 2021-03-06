def make_tree(items1, items2):
    return {
        'type': 'root',
        'children': build(items1, items2)
    }


def build(data1, data2):
    result = []
    keys = set(list(data1.keys()) + list((data2.keys())))

    for key in sorted(keys):
        if key not in data2:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })
        elif key not in data1:
            result.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': build(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            result.append({
                'key': key,
                'type': 'changed',
                'value1': data1[key],
                'value2': data2[key]
            })
        else:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key],
            })
    return result

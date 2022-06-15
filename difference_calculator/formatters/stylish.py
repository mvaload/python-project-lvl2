def render(tree):
    return prepare_format(tree)


def prepare_format(node, depth=0):
    children = node.get('children')
    indent = build_indent(depth)
    if node['type'] == 'root':
        lines = map(lambda child: prepare_format(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif node['type'] == 'added':
        return f"{indent}+ {node['key']}: {stringify(node.get('value'), depth)}"
    elif node['type'] == 'deleted':
        return f"{indent}- {node['key']}: {stringify(node.get('value'), depth)}"
    elif node['type'] == 'changed':
        lines = [
            f"{indent}- {node['key']}: {stringify(node.get('value1'), depth)}",
            f"{indent}+ {node['key']}: {stringify(node.get('value2'), depth)}"
        ]
        return '\n'.join(lines)
    elif node['type'] == 'unchanged':
        return f"{indent}  {node['key']}: {stringify(node.get('value'), depth)}"
    elif node['type'] == 'nested':
        lines = map(lambda child: prepare_format(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node['key']}: {{\n{result}\n{indent}  }}"
    else:
        raise Exception(f"Unknown type: {node['type']}")


def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringify(data, depth):
    if bool == type(data):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    if dict == type(data):
        parts = []
        for key in data:
            indent = build_indent(depth + 1)
            parts.append(f"{indent}  {key}: {stringify(data[key], depth + 1)}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"

    return data

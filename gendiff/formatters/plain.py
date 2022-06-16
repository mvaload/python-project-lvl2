def render(tree):
    return prepare_format(tree)


def prepare_format(node, ancestry=''):
    children = node.get('children')
    property_name = f"{ancestry}{node.get('key')}"

    if node['type'] == 'root':
        parts = map(lambda child: prepare_format(child), children)
        lines = sum(parts, [])
        return '\n'.join(lines)
    elif node['type'] == 'nested':
        parts = map(
            lambda child: prepare_format(child, f"{property_name}."),
            children,
        )
        return sum(parts, [])
    elif node['type'] == 'added':
        return [f"Property '{property_name}' was added with value:"
                f" {stringify(node['value'])}"]
    elif node['type'] == 'deleted':
        return [f"Property '{property_name}' was removed"]
    elif node['type'] == 'changed':
        return [
            f"Property '{property_name}' was updated. "
            f"From {stringify(node['value1'])} to {stringify(node['value2'])}"
        ]
    elif node['type'] == 'unchanged':
        return []
    else:
        raise Exception(f"Unknown type: {node['type']}")


def stringify(value):
    if bool == type(value):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if str == type(value):
        return f"'{value}'"

    if dict == type(value) or list == type(value):
        return "[complex value]"

    return value

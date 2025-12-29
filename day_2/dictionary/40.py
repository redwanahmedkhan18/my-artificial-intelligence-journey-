#Flatten nested dictionary
nested_dict = {
    'A': {
        'B': {
            'C': 1,
            'D': 2
        },
        'E': 3
    },
    'F': 4
}


flat_dict = {}


def flatten_dict(nested, parent_key='', separator="_"):
    items = {}
    for k, v in nested.items():
        key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, key, separator))
        else:
            items[key] = v
    return items

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)

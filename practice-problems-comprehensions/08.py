dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# Method 1

lst = []
for name, info in dict1.items():
    type = info['type']
    colors = info['colors']
    size = info['size']

    if type == 'fruit':
        lst.append([color.capitalize() for color in colors])
    elif type == 'vegetable':
        lst.append(size.upper())

print(lst)

# Method 2

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    elif item['type'] == 'vegetable':
        return item['size'].upper()

lst = [transform_item(info) for info in dict1.values()]
print(lst)
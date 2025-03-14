def order_by_value(my_dict):
    keys = list(my_dict.keys())
    return sorted(keys, key=my_dict.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
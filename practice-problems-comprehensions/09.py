lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# [{e: [8], f: [6, 10]}]

def is_all_even(d):
    return all([ele % 2 == 0 for value in d.values()
                             for ele in value])

new_lst = [d for d in lst if is_all_even(d)]
print(new_lst)
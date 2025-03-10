lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# Method 1

lst_new = []
for ele in lst:
    lst_new.append(sorted(ele))

print(lst_new)

# Method 2

lst_new = [sorted(ele) for ele in lst]
print(lst_new)
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

# Method 1

lst_new = []
for ele in lst:
    lst_new.append(sorted(ele, key=str))

print(lst_new)

# Method 2

lst_new = [sorted(ele, key=str) for ele in lst]
print(lst_new)
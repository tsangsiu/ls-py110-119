a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

'''
a -> 2
b -> [5, 8] -> [3, 8]
lst -> [a, b] -> [4, b]

The final values of `a` and `b` are `2` and `[3, 8]` respectively.
'''
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

def sum_of_odd_numbers(lst):
    return sum([ele for ele in lst if ele % 2 == 1])

sorted_lst = sorted(lst, key=sum_of_odd_numbers)
print(sorted_lst)
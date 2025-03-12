def multiply_list(lst1, lst2):
    mult_lst = []
    for idx in range(len(lst1)):
        mult_lst.append(lst1[idx] * lst2[idx])
    
    return mult_lst

def multiply_list(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
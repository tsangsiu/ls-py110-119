def interleave(lst1, lst2):
    lst_interleave = []

    for idx, _ in enumerate(list1):
        lst_interleave.append(lst1[idx])
        lst_interleave.append(lst2[idx])

    return lst_interleave

def interleave(lst1, lst2):
    return [ele for tup in zip(lst1, lst2)
                for ele in tup]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
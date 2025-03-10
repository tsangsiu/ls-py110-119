lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# [[], [3, 12], [9], [15, 18]]

# Method 1

new_lst = []
for sub_lst in lst:
    new_sub_lst = []
    for ele in sub_lst:
        if ele % 3 == 0:
            new_sub_lst.append(ele)

    new_lst.append(new_sub_lst)

print(new_lst)

# Method 2

new_lst = [[ele for ele in sub_lst if ele % 3 == 0]
                for sub_lst in lst]
print(new_lst)
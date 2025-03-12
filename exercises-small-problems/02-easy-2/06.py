def multiplicative_average(lst):
    product = 1
    for num in lst:
        product *= num

    multiplicative_average = product / len(lst)
    return f'{multiplicative_average:.3f}'

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
def halvsies(lst):
    half = (len(lst) + 1) // 2
    return [lst[:half], lst[half:]]




print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])         # len: 4; 0-1, 2-3
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])   # len: 5; 0-2, 3-4
print(halvsies([5]) == [[5], []])                         # len: 1; 0, 1
print(halvsies([]) == [[], []])                           # len: 0; 
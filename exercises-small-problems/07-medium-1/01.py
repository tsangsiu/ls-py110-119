'''

[P]
- Rules
  - Explicit
    - Write a function named `rotate_list` that rotates a list
      by moving the first element to the end of the list
    - Do not modify the original list
    - If the input is an empty list, return an empty list
    - If the input is not a list, return `None`

- Input: List
- Output: A new list

[E]

[D]

[A]
- Check if the input is a list, if not, return `None`
- If the input list contains 0 or 1 element,
  - return a copy of the list
- Else,
  - Slice the input list from the 2nd element till the end
  - Append the first element to the above sliced list
  - Return the resultant list

'''

def rotate_list(lst):
    if type(lst) is not list:
        return None

    if len(lst) <= 1:
        return lst.copy()
    else:
        return lst[1:] + [lst[0]]

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
'''
Write a function that takes a list of numbers and returns a lis
 with the same number of elements, but with each element's value
   being the running total from the original list.

[P]
- Input: List
- Output: List
- Rules:
    - Explicit:
        - Return a (new?) list of running total
    - Implicit:
        - If a list passed in is empty, return an empty list

[E]

[D]
- Intermediate: List

[A]
- Initialize `running_total` to an empty list
- Iterate through the list passed in
    - If `running_total` is empty,
        - Append the current number to `running_total`
    - Else,
        - Add the current number to the last number in `running_total`
        - Append the sum to `running_total`
- Return `running_total`

'''

def running_total(lst):
    running_total = []
    for num in lst:
        if running_total == []:
            running_total.append(num)
        else:
            running_total.append(num + running_total[-1])

    return running_total

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
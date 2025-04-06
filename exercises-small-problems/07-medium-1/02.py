'''

[P]
- Rules
  - Explicit
    - Write a function that rotates the last `count` digits of a `number`
    - Move the first of the digits that we want to rotate to the end,
      and shift the remaining digits to the left
    - The function name is `rotate_rightmost_digits`
- Input: Two Integers
- Output: An Integer

[E]

[D]

[A]
- Turn the input integers into a list of characters of individual digits
- Separate the list into two parts:
  - The part of digits that do not need rotation
  - The last `count` digits of number
- Use the `rotate_list` function on the second part of the list
- Combine the characters into one string
- Turn the string to an integer
- Return the integer

'''

def rotate_list(lst):
    if type(lst) is not list:
        return None

    if len(lst) <= 1:
        return lst.copy()
    else:
        return lst[1:] + [lst[0]]

def rotate_rightmost_digits(number, count):
    digits_char = list(str(number))
    digits_char = digits_char[:-count] + rotate_list(digits_char[-count:])
    number_char = ''.join(digits_char)
    number = int(number_char)
    return number

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
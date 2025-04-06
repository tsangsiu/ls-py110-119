'''

[P]
- Rules
  - Explicit
    - Write a function named `max_rotation` that takes an integer and
      returns the maximum rotation of that integer
    - We can use the function `rotate_rightmost_digits`

[E]
- Given the number 735291
  -> 735291 -> 352917
  -> 3 52917 -> 3 29175
  -> 32 9175 -> 32 1759
  -> 321 759 -> 321 597
  -> 3215 97 -> 3215 79
  -> 32157 9 -> 32157 9
  -> 321579

[D]

[A]
- Initialize `n_digits` to the number of digits of the input number
- From `n_digits` down to 1,
  - Take the current iteration number as `count`
  - Apply the function `rotate_rightmost_digits` with arguments `number` and `count`
  - Save the return value to `number`
- Return the final `number`

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

def max_rotation(number):
    n_digits = len(str(number))
    for count in range(n_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)
    return number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
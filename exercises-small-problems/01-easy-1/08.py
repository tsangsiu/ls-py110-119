'''

[P]
- Input: String
- Output: Integer
- Rules:
    - Explicit
        - Convert the string representation of an integer to an integer
        - Do not use any of the standard conversion function in Python
        - Need not worry about the + or - signs
        - Need not worry about invalid characters
        - All characters are numeric

[E]

[D]
- Intermediate: A list to store the individual digits

[A]
- Initialize `digits_str` to the string `0123456789`
- Split the given string to a list of individual digits
- Assign the above list to `digits`
- Reverse `digits`
- Initialize `int_` to 0
- Iterate through `digits` with index
    - Convert the character digit to digit by looking for the index in `digits_str`
    - Increment `int_` by `digit` * 10**current index
- Return `int_`
    
'''

def string_to_integer(int_str):
    digits_str = '0123456789'

    int_ = 0
    digits = reversed(list(int_str))

    for idx, digit in enumerate(digits):
        int_ += digits_str.index(digit) * 10**idx

    return int_

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# Further Exploration

def hexadecimal_to_integer(s):
    digits_str = '0123456789ABCDEF'

    value = 0
    digits = reversed(list(s))

    for idx, digit in enumerate(digits):
        value += digits_str.index(digit.upper()) * 16**idx

    return value

print(hexadecimal_to_integer('4D9f') == 19871)  # True
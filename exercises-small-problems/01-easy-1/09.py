'''

[P]
- Input: String
- Output: Integer
- Rules:
    - Explicit
        - Convert the string representation of an integer to an integer
        - Do not use any of the standard conversion function in Python
        - The string may have a leading + or - sign
        - Return a negative number is there is a leading - sign
        - Return a positive number is there is a leading + sign or no leading sign
        - Need not worry about invalid characters
        - All characters are numeric
        - The string will always contain a valid number

[E]

[D]
- Intermediate: A list to store the individual digits

[A]
- If the leading sign is +
    - Convert the string from index 1 onwards to integer
    - Return the integer
- Else if the leading sign is -
    - Convert the string from index 1 onwards to integer
    - Multiply the integer by -1
    - Return the integer
- Else
    - Convert the string to integer
    - Return the integer

-- string_to_integer --
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

def string_to_signed_integer(s):
    if s[0] == '+':
        return string_to_integer(s[1:])
    elif s[0] == '-':
        return string_to_integer(s[1:]) * -1
    else:
        return string_to_integer(s)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
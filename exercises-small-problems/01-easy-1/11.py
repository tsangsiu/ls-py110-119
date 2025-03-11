'''

[P]
- Input: Non-negative integer
- Output: String representation of the integer
- Rule:
    - Explicit:
        - Convert an integer value to the string representation
          of that integer
        - Do not use any of the standard conversion function in Python
        - The integer could be a negative number
    - Implicit:
        - If the input number is positive, prepend a '+' sign

[E]

[D]

[A]
-- signed_integer_to_string --
- If the given number is negative,
    - Multiply the input number by -1
    - Get the string representation of the result number by using `integer_to_string`
    - Prepend '-' to the above string
    - Return the string
- Else if the given number is positive,
    - Get the string representation of the number by using `integer_to_string`
    - Prepend '+' to the above string
    - Return the string 
- Else,
    - Return '0'

-- integer_to_string --
- Consider the digits from the rightmost digit to the leftmost digit
- Initialize `int_to_str` to `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']`
- Initialize `int_str` to an empty string

- Loop
    - Get the rightmost digit by dividing the number by 10 and obtain the remainder
    - Reassign the parameter variable to the number with the units digit
      by obtaining the quotient when integer divided by 10
    - Get the str representation of the quotient by obtaining the corresponding 
        element from `int_to_str`
    - Left append that string to the left of `int_str`
    - If the quotient is 0,
        - Break the loop

- Return `int_str`

'''

def integer_to_string(int_):
    int_to_str = list('0123456789')
    int_str = ''

    while True:
        rightmost_digit = int_ % 10
        int_ //= 10
        int_str = int_to_str[rightmost_digit] + int_str
        if int_ == 0:
            break

    return int_str

def signed_integer_to_string(int_):
    if int_ < 0:
        return f'-{integer_to_string(-int_)}'
    elif int_ > 0:
        return f'+{integer_to_string(int_)}'
    else:
        return '0'


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
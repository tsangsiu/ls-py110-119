'''

[P]
- Input: Non-negative integer
- Output: String representation of the integer
- Rule:
    - Explicit:
        - Convert a non-negative integer value to the string representation
          of that integer
        - Do not use any of the standard conversion function in Python

[E]

[D]

[A]
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

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
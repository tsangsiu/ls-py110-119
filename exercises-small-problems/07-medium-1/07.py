'''

[P]
- Rules
  - Explicit
    - The first two numbers of a Fibonacci series are 1 and 1
    - Every number in the series is the sum of the previous two
    - Write a function called `fibonacci` that computes the nth Fibonacci number
    - `nth` is the argument passed to the function

[E]

[D]
- Input: Integer
- Output: Integer

[A]
- Initilize `series` to the list `[1, 1]`
- If `nth` is 1 or 2,
  - Return 1
- Else
  - Loop
    - Calculate the sum of the last two integers in `series`
    - Append the sum to `series`
    - If the length of `series` == `nth`,
      - Break
  - Return the last integer in `series`

'''

def fibonacci(nth):
    series = [1, 1]

    if nth == 1 or nth == 2:
        return 1
    
    while True:
        next_number = series[-2] + series[-1]
        series.append(next_number)
        if len(series) == nth:
            break

    return series[-1]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
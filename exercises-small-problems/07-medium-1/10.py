'''

[P]
- Rules
  - Explicit:
    - Write a function named `  find_fibonacci_index_by_length`
      that returns the index of the first Fibonacci number
      that has the number of digits specified by the argument
    - The first Fibonacci number has an index of 1
    - The argument is always an integer >= 2

[E]

[D]
- Intermediate: A list to store the numbers in the series

[A]
- Initialize `idx` to 1
- Loop
  - Find the `idx`-th Fibonacci number
  - If the length of the number is the target length,
    - Break the loop
  - Increment `idx` by 1
- Return `idx`

'''

import sys

def fibonacci(nth, mem={}):
    if nth in [1, 2]:
        return 1
    
    if nth - 1 not in mem:
        mem[nth - 1] = fibonacci(nth - 1)
    
    if nth - 2 not in mem:
        mem[nth - 2] = fibonacci(nth - 2)
    
    return mem[nth - 2] + mem[nth - 1]

def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)

    idx = 1
    while True:
        nth_fibonacci_number = fibonacci(idx)
        if len(str(nth_fibonacci_number)) == length:
            break
        
        idx += 1
    
    return idx

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
'''

[P]
- Rules
  - Explicit
    - Write a function named `is_prime` that takes a positive integer, and
      return true if the number is primt, false if not prime
    - Not allowed to use any of Python's packages

[E]

[D]

[A]
- If the input integer is 1,
  - Return `False`
- Else iterate through 2 to 1 less then the input integer,
  - If input integer is dividible by the current number,
    - Return `False`

- Return `True`

'''

def is_prime(number):
    if number == 1:
        return False
    
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
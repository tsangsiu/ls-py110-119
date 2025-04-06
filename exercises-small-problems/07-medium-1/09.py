def fibonacci(nth, mem={}):
    if nth in [1, 2]:
        return 1
    
    if nth - 1 not in mem:
        mem[nth - 1] = fibonacci(nth - 1)
    
    if nth - 2 not in mem:
        mem[nth - 2] = fibonacci(nth - 2)
    
    return mem[nth - 2] + mem[nth - 1]

def fibonacci(nth, mem={}):
    if nth <= 2:
        return 1
    elif nth in mem:
        return mem[nth]
    else:
        mem[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return mem[nth]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(100))
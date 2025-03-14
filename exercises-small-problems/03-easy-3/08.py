def sequence(count, start_num):
    lst = []
  
    for i in range(1, count + 1):
        lst.append(start_num * i)

    return lst

def sequence(count, start_num):
    return [start_num * i for i in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
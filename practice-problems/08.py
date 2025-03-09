statement = "The Flintstones Rock"

counts = {}
statement = statement.replace(' ', '')
for char in statement:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)
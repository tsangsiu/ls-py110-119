dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Method 1

list_of_vowels = []
for value in dict1.values():
    for word in value:
        for char in word:
            if char in 'aeiou':
                list_of_vowels.append(char)

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Method 2

list_of_vowels = [char for value in dict1.values()
                       for word in value
                       for char in word if char in 'aeiou']

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
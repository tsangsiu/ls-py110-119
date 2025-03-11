'''

[P]
- Input: String
- Output: Dictionary
- Rules:
    - Explicit
        - Write a function that takes a string, which consists of 0 or more
          space-separated words
        - Return a dictionary of counts of words of different sizes
        - Count only the letters (i.e., the length of it's is 3, not 4)
    - Implicit
        - Return an empty dictionary for an empty string

[E]

[D]
- Intermediate: a list to store individual words

[C]
- Split the string into words at space
- Assign the above resultant list to `words`
- Initialize an empty dictionary to `counts`
- Iterate through every word in `words`
    - initialize `length` to 0
    - Iterate through every char in the current word
        - If the current character is an alphabet
            - Increment `length` by 1
    - Update the dictionary
- Return the dictionary

'''

def word_sizes(string):
    words = string.split()
    counts = {}

    for word in words:
        length = 0
        for char in word:
            if char.isalpha():
                length += 1
        counts[length] = counts.get(length, 0) + 1

    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
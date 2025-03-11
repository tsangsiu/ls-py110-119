'''

[P]
- Input: String
- Output: Dictionary
- Rules:
    - Explicit
        - Write a function that takes a string, which consists of 0 or more
          space-separated words
        - Return a dictionary of counts of words of different sizes
        - Words consist of any sequence of non-space characters
    - Implicit
        - Return an empty dictionary for an empty string
        - 'seven.' is of size 6

[E]

[D]
- Intermediate: a list to store individual words

[C]
- If the string passed in is an empty string,
    - Return an empty dictionary
- Split the string into words at space
- Assign the above resultant list to `words`
- Initialize an empty dictionary to `counts`
- Iterate through every word in `words`
    - Get the length of the current word
    - Update the dictionary
- Return the dictionary

'''

def word_sizes(string):
    if string == '':
        return {}

    words = string.split(' ')
    counts = {}

    for word in words:
        length = len(word)
        counts[length] = counts.get(length, 0) + 1

    return counts

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
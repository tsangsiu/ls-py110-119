'''

[P]
- Input: String
- Output: String
- Rules:
    - Explicit:
        - Given a string of words separated by space,
          swap the first and last letters of each word
        - Each word contains at least one letter
        - The given string will always contain one word
        - There are no leading, trailing, or repeated spaces
    - Implicit

[E]

[D]
- Intermediate: A list to store the words

[A]
- Split the given string at space
- Assign the above list to `words`
- Iterate through every word in `words`
    - Swap the first and the last letter
    - Replace the current element in the list with the swapped word
- Join the words in `words` by a space to form a string
- Return the string

- Swapping
    - If the word is of length 1,
        - Keep if as it is
    - Else,
        - Concatenate the last char, middle char, and first char

'''

def swap(string):
    words = string.split()

    for idx, word in enumerate(words):
        if len(word) == 1:
            pass
        else:
            words[idx] = word[-1] + word[1:-1] + word[0]

    return ' '.join(words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
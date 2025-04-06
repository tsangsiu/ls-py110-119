'''
[P]
- Rules
  - Explicit
    - Write a function named `word_to_digit` that takes a string as an argument, and
      returns that string with every "number word" converted to its corresponding
      digit character
    - Assume that the string does not contain any punctuation

[E]

[D]
- Input: String
- Intermediate: List
- Output: String

[A]
- Create a dictionary that maps every "number word" to its digit character
- Split the input string into a list of words at space
- Iterate through the list
  - If the current element is a "number word",
    - Transform it to its corresponding digit character using the dictionary
- Combine the list to form one single string
- Return the string

'''

def word_to_digit(message):
    WORD_TO_DIGIT = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

    words = message.split()
    for idx, word in enumerate(words):
        if word in WORD_TO_DIGIT:
            words[idx] = WORD_TO_DIGIT[word]

    message = ' '.join(words)
    return message

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# Further Exploration
def word_to_digit(message):
    WORD_TO_DIGIT = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

    for word in WORD_TO_DIGIT:
        message = message.replace(word, WORD_TO_DIGIT[word])

    return message

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
'''

[P]
- Input: String
- Output: Boolean
- Rules:
    - Explicit
        - If the string passed is a palindrome, return True, False if otherwise
        - A palindrome reads the same forwards and backwards
        - Case matters
        - All characters matter

[E]

[D]
- Input: String
- Intermediate: String
- Output: Boolean

[A]
- Reverse the string passed in
- Compare the revered string to the passed-in string
- Return `True` if they are equal in value, `False` if otherwise

'''

def is_palindrome(string):
    return string[::-1] == string

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
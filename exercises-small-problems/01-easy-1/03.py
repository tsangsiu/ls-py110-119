'''
[P]
- Input: String
- Output: Boolean
- Rules:
    - Explicit
        - If the string passed is a palindrome, return True, False if otherwise
        - A palindrome reads the same forwards and backwards
        - Case does nonot matter
        - Ignore all non-alphanumeric characters

[E]

[D]
Input: String
Intermediate: String
Output: Boolean

[A]
- Turn the whole string to lower case and assigned it to `string`
- Remove non-alphanumeric characters
    - Initialize `string_alphanumeric` to an empty string
    - Iterate through `string`, character by character
        - If the current character is alphanumeric
            - Concatenate to the string `string_alphanumeric`
- Use `is_palindrome` to check if the resultant string is a palindrome
'''

def is_palindrome(string):
    return string[::-1] == string

def is_real_palindrome(string):
    string = string.casefold()

    string_alphanumeric = ''
    for char in string:
        if '0' <= char <= '9' or 'a' <= char <= 'z':
            string_alphanumeric += char
    
    return is_palindrome(string_alphanumeric)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
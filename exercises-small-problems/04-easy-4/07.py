def leading_substrings(string):
    return [string[:(idx + 1)] for idx in range(len(string))]

def substrings(string):
    substrs = []

    for start_idx in range(len(string)):
        substrs.extend(leading_substrings(string[start_idx:]))

    return substrs

def is_palindrome(string):
    return len(string) > 1 and string == string[::-1]

def palindromes(string):
    substrs = substrings(string)
    return [substr for substr in substrs if is_palindrome(substr)]


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
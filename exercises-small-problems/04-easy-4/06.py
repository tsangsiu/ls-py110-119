def leading_substrings(string):
    return [string[:(idx + 1)] for idx in range(len(string))]

def substrings(string):
    substrs = []

    for start_idx in range(len(string)):
        substrs.extend(leading_substrings(string[start_idx:]))

    return substrs

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
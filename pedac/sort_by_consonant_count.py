'''
[P]
Input: A list of strings
Output: A list of sorted strings based on the number of most adjacent consonants
Rules:
  Explicit:
    - Sort a list of strings based on the highes number of adjacent consonants
    - If two strings contain the same highest number of adjacent consonants,
      retain their original order in relation to each other
    - Consonants are considered adjacent if they are next to each other,
      or if there is a space between two consonant in adjacent words.
    - For 'can can', 'n c' is considered adjacent
  Implicit:
    - The individual strings are not just words, they could be words separated 
      by spaces
    - Consonants refers to the alphabets that are not in this list:
      ['a', 'e', 'i', 'o', 'u']
    - Strings may contain single or multiple words
    - Strings may not be empty
    - Strings may have no adjacent consonants
    - Strings should be sorted in descending order
    - Case is not relevant

Questions:
- What if there are non-alphabets and spaces in the strings? (e.g. '.' and '?') -> dunno
- Is case important? -> dunno
- ascending/ descending order? -> descending
- mutative/ non-mutative?
- based on the test cases, assume that strings cannot be empty

[D]
- Input: List
- Output: List
- A dictionary to store the strings, with the number of adjacent consonants as
  keys. If that number is 0 or 1, group them as one group.

[A]
- Initialize `output_lst` to an empty list
- Initialize `lst_by_most_adj_consonants` to an empty dictionary

- Iterate through the list as an input
  - For each string, calculate the maximum number of adjacent consonants
  - Put the current string in `lst_by_most_adj_consonants` in the appropriate group

- Get the list of keys of `lst_by_most_adj_consonants` by descending order
- Iterate through the list
  - Access the member in the dictionary by the current key
  - Add the elements in order to `output_lst`

- Return `output_lst`

''Calculate the maximum number of adjacent consonants''
- Remove the spaces in the string
- Initialize `max_adj_consonants` to 0
- Intialize `streak` to 0

- Iterate through the characters of the given string
  - If the current character is a consonants
    - Increment `streak` by 1
  - Else if the current character is a non-consonants
    - If `streak` is greater than `max_adj_consonant`
      - Assign `streak` to `max_adj_consonants`
    - Reset `streak` to 0

  - If the current character is the last one
    - If `streak` is greater than `max_adj_consonant`
      - Assign `streak` to `max_adj_consonant`
    
- If `max_adj_consonants` equals 1
  - Return 0
- Else
  - Return `max_adj_consonants`

'''

def count_max_adj_consonants(s):
    s = s.replace(' ', '')

    max_adj_consonants = 0
    streak = 0

    for idx, char in enumerate(s):
        if char not in ['a', 'e', 'i', 'o', 'u']:
            streak += 1
        else:
            if streak > max_adj_consonants:
                max_adj_consonants = streak
            streak = 0

        if idx == len(s) - 1 and streak > max_adj_consonants:
            max_adj_consonants = streak
    
    if max_adj_consonants == 1:
        return 0
    else:
        return max_adj_consonants

def sort_by_consonant_count(lst):
    output_lst = []
    lst_by_most_adj_consonants = {}

    for s in lst:
        max_adj_consonants = count_max_adj_consonants(s)
        if max_adj_consonants in lst_by_most_adj_consonants:
            lst_by_most_adj_consonants[max_adj_consonants].append(s)
        else:
            lst_by_most_adj_consonants[max_adj_consonants] = [s]

    counts_in_descending = list(lst_by_most_adj_consonants.keys())
    counts_in_descending.sort(reverse=True)

    for count in counts_in_descending:
        output_lst.extend(lst_by_most_adj_consonants[count])

    return output_lst

print(count_max_adj_consonants('ddd aa') == 3)
print(count_max_adj_consonants('ccaa') == 2)
print(count_max_adj_consonants('baa') == 0)
print(count_max_adj_consonants('aa') == 0)
print(count_max_adj_consonants('rstafgdjecc') == 4)
print(count_max_adj_consonants('xxxx') == 4)

my_list = ['aa', 'baa', 'ccaa', 'dddaa'] 
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
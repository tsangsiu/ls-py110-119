'''

[P]
Input: Numbers, user inputs from the terminal
Output: a `print` message
Rules:
    Explicit:
        - Write a program that accept 6 numbers from the user
        - Print a message stating if the 6-th number is among the first five
    Implicit:
        -

[E]
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.
-----------------------------
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

[D]
- Intermediate: A list to store the numbers input by the user

[A]
- Initialize `numbers` to an empty list
- Accept numbers one by one from the user
- Append the number to `numbers`
- Check if the 6-th number is in the list
- Print the result

'''

numbers = []

numbers.append(input('Enter the 1st number: '))
numbers.append(input('Enter the 2nd number: '))
numbers.append(input('Enter the 3rd number: '))
numbers.append(input('Enter the 4th number: '))
numbers.append(input('Enter the 5th number: '))
num_6 = input('Enter the last number: ')

if num_6 in numbers:
    print(f'{num_6} is in {','.join(numbers)}.')
else:
    print(f"{num_6} isn't in {','.join(numbers)}.")
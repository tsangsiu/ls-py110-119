def double_consonants(string):
    output_str = ''

    for char in string:
        output_str += char
        if char.isalpha() and char.lower() not in 'aeiou':
            output_str += char

    return output_str

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
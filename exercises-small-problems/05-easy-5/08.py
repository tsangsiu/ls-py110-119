def staggered_case(string):
    output_string = ''

    for idx, char in enumerate(string):
        if idx % 2 == 0:
            output_string += char.upper()
        else:
            output_string += char.lower()

    return output_string



string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
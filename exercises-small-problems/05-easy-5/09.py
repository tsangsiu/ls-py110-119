def staggered_case(string):
    output_string = ''
    upper_switch = True

    for char in string:
        if char.isalpha():
            output_string = output_string + (char.upper() if upper_switch else char.lower())
            upper_switch = not upper_switch
        else:
            output_string += char

    return output_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
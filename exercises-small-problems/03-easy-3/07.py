def swap_name(name):
    first_name, last_name = name.split(' ')
    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Further Exploration

def swap_name(name):
    first_name = name.split(' ')[:-1]
    last_name = name.split(' ')[-1]

    return f'{last_name}, {' '.join(first_name)}'

print(swap_name('Joe Roberts') == "Roberts, Joe")     # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
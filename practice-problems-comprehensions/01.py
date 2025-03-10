munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Method 1

total_age = 0
for member, info in munsters.items():
    age = info['age']
    gender = info['gender']

    if gender == 'male':
        total_age += age

print(total_age)

# Method 2

total_age = sum([info['age'] for info in munsters.values() if info['gender'] == 'male'])
print(total_age)
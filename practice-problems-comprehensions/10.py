import random

def generate_uuid():
    hex_chars = list('0123456789abcdef')
    sections = [8, 4, 4, 4, 12]

    uuid_sections = [''.join([random.choice(hex_chars) for _ in range(0, section)])
                                                       for section in sections]
    uuid = '-'.join(uuid_sections)

    return uuid

print(generate_uuid())
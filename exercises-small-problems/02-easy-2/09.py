def print_occurrences(counts):
    for ele, count in counts.items():
        print(f'{ele} => {count}')

def count_occurrences(lst):
    counts = {}

    for ele in lst:
        counts[ele] = counts.get(ele, 0) + 1

    print_occurrences(counts)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Further Exploration

def count_occurrences(lst):
    counts = {}

    for ele in lst:
        ele = ele.lower()
        counts[ele] = counts.get(ele, 0) + 1

    print_occurrences(counts)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

count_occurrences(vehicles)
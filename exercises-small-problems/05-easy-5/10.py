def unique_sequence(seq):
    unique_seq = [seq[0]]

    for ele in seq[1:]:
        if ele != unique_seq[-1]:
            unique_seq.append(ele)

    return unique_seq

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
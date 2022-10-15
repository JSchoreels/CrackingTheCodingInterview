def letters_and_numbers(arr):
    delta_letters_number = 0
    first_occurences = {0: -1}
    max_gap, max_gap_position = 0, -1
    for i in range(len(arr)):
        current = arr[i]
        if current == 'A':
            delta_letters_number += 1
        elif current == 'B':
            delta_letters_number -= 1
        else:
            raise ValueError("Unexpected Value")
        if delta_letters_number in first_occurences and (curr_gap := i - first_occurences[delta_letters_number]) > max_gap:
            max_gap = curr_gap
            max_gap_position = first_occurences[delta_letters_number]
        elif delta_letters_number not in first_occurences:
            first_occurences[delta_letters_number] = i
    return (max_gap, max_gap_position+1)


t1 = letters_and_numbers(list('ABAABABAAAB'))
print(t1)
assert t1 == (6,1)
t2 = letters_and_numbers(list('BABAABABAAAB'))
print(t2)
assert t2 == (8,0)
class PatternPosition:
    def __init__(self, prev_a_count, prev_b_count):
        self.prev_a_count = prev_a_count
        self.prev_b_count = prev_b_count


def pattern_matching(pattern, value):  # assumptions : there is at least one a, if not, b means a
    a_positions = []
    b_positions = []
    prev_a_count = 0
    prev_b_count = 0
    for i, letter in enumerate(pattern):
        if letter == 'a':
            a_positions.append(PatternPosition(prev_a_count, prev_b_count))
            prev_a_count += 1
        elif letter == 'b':
            b_positions.append(PatternPosition(prev_a_count, prev_b_count))
            prev_b_count += 1
        else:
            raise ValueError(f"Wrong Pattern : {letter}")
    N_a = len(a_positions)
    N_b = len(b_positions)
    if N_a == 0:
        if N_b == 0:
            raise ValueError("Empty Pattern")
        a_positions, b_positions = b_positions, a_positions
        N_a, N_b = N_b, N_a


    def are_all_equals(positions, size):
        for i in range(0, size):
            current = value[positions[0].prev_a_count * size_a + positions[0].prev_b_count * size_b + i]
            for i_position in range(1, len(positions)):
                position = positions[i_position]
                new_current = value[position.prev_a_count * size_a + position.prev_b_count * size_b + i]
                if current != new_current:
                    return False
                current = new_current
        return True

    def is_valid_candidate(size_a, size_b):
        # validate all a are the same
        print(f"Validating size_a:{size_a} and size_b:{size_b}")
        return are_all_equals(a_positions, size_a) and are_all_equals(b_positions, size_b)

    for size_a in range(1, len(value) // N_a):  # If value is size 10 and N_a = 3, can't have more than size 3 for it
        if N_b == 0:
            size_b = 0
        elif (len(value) - size_a * N_a) % N_b == 0:  # Don't consider this size_a if we can't divide the rest by N_b
            size_b = (len(value) - size_a * N_a) // N_b
        else:
            continue
        if is_valid_candidate(size_a, size_b):
            return True
    return False

print(f"pattern_matching('aabab', 'catcatgocatgo') : {pattern_matching('aabab', 'catcatgocatgo')}")
print(f"pattern_matching('ab', 'catcatgocatgo') : {pattern_matching('ab', 'catcatgocatgo')}")
print(f"pattern_matching('a', 'catcatgocatgo') : {pattern_matching('a', 'catcatgocatgo')}")
print(f"pattern_matching('b', 'catcatgocatgo') : {pattern_matching('b', 'catcatgocatgo')}")
print(f"pattern_matching('ba', 'catcatgocatgo') : {pattern_matching('ba', 'catcatgocatgo')}")
print(f"pattern_matching('aba', 'catcatgocatgo') : {pattern_matching('aba', 'catcatgocatgo')}")
print(f"pattern_matching('abab', 'catgocatgo') : {pattern_matching('abab', 'catgocatgo')}")

def get_bit(n, i_lsb):
    return int("{:032b}".format(n)[-1-i_lsb])

def missing_number(ints):
    i_bit = 0
    result = 0
    while i_bit < 32:
        arr_0 = []
        arr_1 = []
        for i in range(0, len(ints)):
            if get_bit(ints[i], i_bit) == 0:
                arr_0.append(ints[i])
            else:
                arr_1.append(ints[i])
        if len(arr_0) > len(arr_1):
            result += 2**i_bit
            ints = arr_1
        else:
            ints = arr_0
        i_bit += 1
    return result

assert missing_number([0,1,2,3,4,5,6,7,8,9,10]) == 11
assert missing_number([0,1,2,3,4,5,7,8,9,10]) == 6
assert missing_number([0,1,3,4,5,6,7,8,9,10]) == 2
assert missing_number([1,2,3,4,5,6,7,8,9,10]) == 0
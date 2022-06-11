# 5.4
# Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation.

# Ex : 10110 (22) : largest 11001 (25) : smallest : 10101 (21)
# p = 3
import math
import unittest


def get_next(integer):
    bit_repr = bin(integer).split('b')[1]
    p = get_index_non_trailing_bit(bit_repr)
    # 010 => 2
    # 111 => None
    # 000 => None
    # 100 => None
    # In all those cases, there is no next bigger with same number of 1.
    if not p:
        if math.log2(integer) - round(math.log2(integer)) < 10e-10:
            return 2*integer
        raise ValueError("No next possible")
    count_1 = sum([int(bit) for bit in bit_repr[-1-p:]]) - 1
    integer &= (-1 << p) # p_reverse > 0 since non trailing. It sets everything from end to p excluded to 0
    integer |= 1 << p # it sets position p to 1
    integer |= 2**count_1-1 # it sets count_1 times 1 to the right
    return integer

def get_prev(integer):
    bit_repr = bin(integer).split('b')[1]
    p = get_index_non_trailing_bit(bit_repr, '1')
    # 101 => 2
    # 111 => None
    # 000 => None
    # 100 => None
    # In all those cases, there is no next bigger with same number of 1.
    if not p:
        if math.log2(integer) - round(math.log2(integer)) < 10e-10:
            return 2*integer
        raise ValueError("No next possible")
    count_0 = len(bit_repr[-1-p:]) - sum([int(bit) for bit in bit_repr[-1-p:]]) - 1
    integer &= (-1 << (p+1)) # p_reverse > 0 since non trailing. It sets everything from end to p included to 0
    integer |= (2**p - 1) & (-1 << count_0)
    return integer

def get_index_non_trailing_bit(bit_repr, bit_type = '0'):
    non_trailing_zero = False
    for i in range(0, len(bit_repr)):
        if bit_repr[-1-i] == ('1' if bit_type == '0' else '0'):
            non_trailing_zero = True
        elif non_trailing_zero:
            return i
    return None

class TestCase(unittest.TestCase):
    def test_next_bigger(self):
        self.assertEqual(bin(25), bin(get_next(22)))
        self.assertEqual(bin(32), bin(get_next(16)))
        self.assertRaises(ValueError, lambda: bin(get_next(0)))
        self.assertRaises(ValueError, lambda: bin(get_next(-1)))

    def test_next_smaller(self):
        self.assertEqual(bin(21), bin(get_prev(22)))
        self.assertEqual(bin(8), bin(get_prev(16)))
        self.assertRaises(ValueError, lambda: bin(get_prev(0)))
        self.assertRaises(ValueError, lambda: bin(get_prev(-1)))
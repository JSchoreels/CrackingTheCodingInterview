# Conversion: Write a function to determine the number of bits you would need to flip to convert
# 5.6
# integer A to integer B.
# EXAMPLE
# Input:29 (or: 11101), 15 (or: 01111)
# Output:2

# 1 1 => 0
# 1 0 => 1
# 0 1 => 1
# 0 0 => 0
import unittest


def conversion(int1, int2):
    assert int1 >= 0 and int2 >= 0
    xor = int1 ^ int2
    count_1 = 0
    while xor != 0:
        count_1 += xor & 1
        xor >>= 1
    return count_1 - xor

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(2, conversion(29, 15))
        self.assertEqual(0, conversion(1, 1))
        self.assertEqual(2, conversion(2, 16))
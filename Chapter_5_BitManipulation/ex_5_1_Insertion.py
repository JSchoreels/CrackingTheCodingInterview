# 5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
# j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
import unittest


def insertion(N, M, j, i):
    M_shifted = M << i
    return M_shifted + (N & (-1 << (j + 1)) | N & ((1 << i) - 1) )


class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(0b1010100101, insertion(0b1010101011, 0b010, 4, 1))
        self.assertEqual(0b1010111111, insertion(0b1010101011, 0b1111, 4, 1))
        self.assertEqual(0b1010100100, insertion(0b1010101010, 0b010, 4, 1))
        self.assertEqual(0b1010111110, insertion(0b1010101010, 0b1111, 4, 1))
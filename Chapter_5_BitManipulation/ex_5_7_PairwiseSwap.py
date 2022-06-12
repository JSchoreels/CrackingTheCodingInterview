# 5.7 Pairwise swap
# Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit O and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
# ex :
# 101010 => 010101
# 000000 => 000000
# 111111 => 111111
# ABCDEF & 101010 = A0C0E0 >>1= 0A0C0E
# 01100110 : 10011001
import unittest


def pairwise_swap(n):
    assert n < 2**32
    mask = 0b10101010101010101010101010101010
    a = (mask & n) >> 1
    b = (n << 1) & mask
    return a | b


class TestCase(unittest.TestCase):
    def test_pairwise_swap(self):
        self.assertEqual(85, pairwise_swap(170))
        self.assertEqual(2886, pairwise_swap(1929))
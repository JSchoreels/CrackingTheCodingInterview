# 5.3
# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of ls you could create.
# EXAMPLE
# Input:1775
# Output:8
import unittest


def flip_bit_to_win(integer, max_gap_size = 1):
    bit_repr = bin(integer).split('b')[1]
    prev_block_size = 0
    curr_block_size = 0
    gap_size = 0
    result = 0
    for bit in bit_repr:
        if bit == '0':
            if curr_block_size > 0 and prev_block_size > 0:
                result = max(result, curr_block_size + prev_block_size + gap_size)
                prev_block_size = curr_block_size
                curr_block_size = 0
                gap_size = 0
            if gap_size >= max_gap_size:
                prev_block_size = 0
                curr_block_size = 0
            gap_size += 1
        else:
            if gap_size == 0:
                prev_block_size += 1
            elif gap_size > 0 and prev_block_size > 0:
                curr_block_size += 1
            elif gap_size > 0 and prev_block_size == 0:
                gap_size = 0
                prev_block_size += 1
    if curr_block_size > 0 and prev_block_size > 0:
        result = max(result, curr_block_size + prev_block_size + gap_size)
    return result

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(8, flip_bit_to_win(0b11011101111, max_gap_size=1))
        self.assertEqual(9, flip_bit_to_win(0b110111001111, max_gap_size=2))
        self.assertEqual(7, flip_bit_to_win(0b1000001011, max_gap_size=5))
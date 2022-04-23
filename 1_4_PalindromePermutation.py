# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A
# palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters.
#
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: “taco cat”. “atco cta”. etc.)
import unittest
import math


def is_palindrome_permutation(string):
    occurences = 0
    for char in string:
        if char.is_alpha():
            lower_char = char.lower()
            char_pos = ord(lower_char) - ord('a')
            occurences ^= (1 << char_pos)
    if occurences == 0:
        return True
    return math.fabs(math.log(occurences, 2)) < 1e-8



class DemoTestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome_permutation("Taco cat"))
        self.assertTrue(is_palindrome_permutation("Tco oct"))
        self.assertTrue(is_palindrome_permutation("Tacacat"))
        self.assertTrue(is_palindrome_permutation("aaa"))
        self.assertTrue(is_palindrome_permutation("aabb"))
        self.assertFalse(is_palindrome_permutation("aacabb"))
        self.assertFalse(is_palindrome_permutation("ca"))


unittest.main()
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
        if char.isalpha():
            lower_char = char.lower()
            char_pos = ord(lower_char) - ord('a')
            occurences ^= (1 << char_pos)
    if occurences == 0:
        return True
    float_log = math.log(occurences, 2)
    return occurences == 2**round(float_log)


assert is_palindrome_permutation("Taco cat")
assert is_palindrome_permutation("Tco oct")
assert is_palindrome_permutation("Taczcat")
assert is_palindrome_permutation("aaa")
assert is_palindrome_permutation("aabb")
assert not is_palindrome_permutation("aacabb")
assert not is_palindrome_permutation("ca")
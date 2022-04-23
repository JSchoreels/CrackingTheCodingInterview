#  Problem:
#    There are three types of edits that can performed on strings:
#    insert a character, remove a character, or replace a character.
#    Given two strings, write a function to check if they are one edit (or zero edits) away.
#
#  Example:
#    pale, ple   -> true
#    pales, pale -> true
#    pale, bale  -> true
#    pale, bake  -> false
#
#  Solution:
#    complexity: O(n)
import math

def one_away(str1, str2):
    if len(str1) == len(str2):  # can only be an edit
        edit_still_allowed = 1
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if edit_still_allowed > 0:
                    edit_still_allowed -= 1
                else:
                    return False
    else:
        if math.fabs(len(str1) - len(str2)) > 1:
            return False
        if len(str1) < len(str2):
            str1, str2 = str2, str1  # Now, str1 will be longer than str2
            insertion_met = 0
            for i in range(len(str1)):
                if str1[i] != str2[i-insertion_met]:
                    if insertion_met < 1:
                        insertion_met += 1
                    else:
                        return False
    return True

assert one_away("abcd", "acd")
assert one_away("acd", "abcd")
assert one_away("abcd", "abed")
assert not one_away("abcd", "abcdef")
assert not one_away("abcdef", "abcd")





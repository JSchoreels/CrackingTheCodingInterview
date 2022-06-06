# 5.2 Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at
# most 32 characters, print"ERROR".
import unittest


def binary_to_string(double):
    assert 0 < double < 1
    repr = '0.'
    index = 1
    while double > 1e-10 and index <= 32:
        if double >= 0.5**index:
            double -= 0.5**index
            repr += '1'
        else:
            repr += '0'
        index += 1
    if index == 33 and double > 1e-10:
        raise ValueError("Could not get an exact match for decimal")
    return repr

def string_to_double(repr):
    index = 1
    result = 0.
    for char in repr[2:]:
        result += int(char) * 0.5**index
        index += 1
    return result


class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual('0.1', binary_to_string(0.5))
        self.assertEqual('0.11', binary_to_string(0.75))
        self.assertEqual('0.101', binary_to_string(0.625))
        expected = 0.666666
        self.assertEqual('0.10101010101010101001111101111011', binary_to_string(expected))
        result = string_to_double(binary_to_string(expected))
        print(result)
        print(expected-result)
        self.assertRaises(ValueError, lambda: binary_to_string(0.66666666666666))
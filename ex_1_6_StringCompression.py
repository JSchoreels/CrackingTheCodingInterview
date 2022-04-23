# String compression : Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string "aabccccaaaa" would become "a2b1c5a3". If the "compressed" string would not become smaller
# than the original string,"" your method should return the original string. You can assume the string has only uppercase
# and lower case letters (a-z)

def compression(string):
    compressed = [0] * len(string)
    successive_counter = 1
    compressed_index = 0
    if len(string) <= 2: ## only useful to compress if we have 3-letter string
        return string
    for i in range(1, len(string) + 1): # One more element to to add the latest element in the string
        if i < len(string) and string[i] == string[i-1]:
            successive_counter += 1
        else:
            compressed[compressed_index] = string[i-1]
            compressed_index += 1
            if successive_counter > 1: # if it's 1, just put the char and nothing more
                for digit in str(successive_counter):
                    compressed[compressed_index] = digit
                    compressed_index += 1
                successive_counter = 1
    compressed_size = compressed_index
    if compressed_size < len(string):
        return "".join(compressed[0:compressed_size])
    else:
        return string

assert compression("abcde") == "abcde"
assert compression("a") == "a"
assert compression("aa") == "aa"
assert compression("aaa") == "a3"
assert compression("aabbcc") == "aabbcc"
assert compression("aabbccc") == "a2b2c3"
assert compression("a"*15+"b"*5) == "a15b5"
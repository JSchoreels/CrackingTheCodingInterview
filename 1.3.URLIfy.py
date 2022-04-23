# 1.3 : URLify: Write a method to replace all spaces in a string with "%20". You may assume that the string has
# sufficient space at the end to hold the additional characters, and that you are given the "true" length of the
# string. "Note: if implement in Java, please us a character array so that you can perform this operation in place"
# EXAMPLE
# Input : "Mr John Smith    ", 13
# Output : "Mr%20John%20Smith"


input = list("Mr John Smith    ")
size = 13

def urlify(input, size):
    pattern_input = " "
    pattern_output = "%20"
    pattern_size_delta = len(pattern_output) - len(pattern_input) # here 2
    output_size = size
    for char in input[0:size]:
        if char == " ":
            output_size += pattern_size_delta
    if output_size == size:
        return input
    new_index = output_size - 1
    old_index = size - 1
    while(new_index >= 0 and old_index >= 0):
        if input[old_index] != " ":
            input[new_index] = input[old_index]
            new_index -= 1
            old_index -= 1
        else:
            for pattern_index in range(len(pattern_output)):
                input[new_index] = pattern_output[-1-pattern_index]
                new_index -= 1
            old_index -= 1
    assert new_index == old_index == -1
    return input

assert urlify(input, size) == list("Mr%20John%20Smith")
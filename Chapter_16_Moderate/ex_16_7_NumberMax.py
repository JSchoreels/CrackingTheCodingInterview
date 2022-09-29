# 16.7 Number Max: Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.

def number_max(a,b):
    delta_ab = a-b
    ab_sign = get_sign(delta_ab)  # 1 if positive. 0 if negative
    ba_sign = flip(ab_sign)  # Python is quite specific because -1 >> 32 = -1 and N >> 32 = 0 with N<2**32
    return a*ab_sign + b*ba_sign

def number_max_without_overflow(a,b):
    sign_a = get_sign(a)
    sign_b = get_sign(b)
    sign_delta = get_sign(a-b) # 1 if positive. 0 if negative
    use_sign_a = sign_a ^ sign_b # 1 if different sign
    use_sign_delta = flip(use_sign_a) # if the same, we use delta
    choice = sign_a * use_sign_a + sign_delta * use_sign_delta # sign_a if use_sign_a, sign_delta otherwise
    non_choice = flip(choice) # just the opposite
    return a*choice + b*non_choice


def get_sign(n):
    return 1 ^ (1 & (n >> 32)) # Python is quite specific because -1 >> 32 = -1 and N >> 32 = 0 with N<2**32

def flip(sign):
    return 1 ^ sign


print(number_max_without_overflow(1,-5))
print(number_max_without_overflow(-5,1))
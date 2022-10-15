import math
import time

def count_of_2_in_range_naive(n):
    count = 0
    for i in range(n+1):
        tmp = i
        while tmp > 0:
            if tmp % 10 == 2:
                count += 1
            tmp //= 10
    return count

def count_of_2_in_range(n):
    assert n >= 0
    if n < 2:
        return 0
    elif n <= 10:
        return 1
    elif math.fabs(math.log10(n) - math.floor(math.log10(n))) < 1e-8:
        return count_of_2_in_range(n-1)
    else:
        prev_power_10 = math.floor(math.log10(n))
        first_digit_n = n // (10 ** prev_power_10) % 10
        result = 0
        result += count_of_2_in_range(n - (first_digit_n * 10 ** prev_power_10))
        result += first_digit_n * count_of_2_in_range(10 ** prev_power_10)
        if first_digit_n > 2:
            result += 10 ** prev_power_10
        elif first_digit_n == 2:
            result += n - (first_digit_n * 10 ** prev_power_10) + 1
        return result

def count_of_2_in_range_with_memo(n, memo, use_memo=True):
    assert n >= 0
    if use_memo and n in memo:
        return memo[n]
    if n < 2:
        return 0
    elif n <= 10:
        return 1
    else:
        prev_power_10 = math.floor(math.log10(n))
        first_digit_n = n // (10 ** prev_power_10) % 10
        result = 0
        result += count_of_2_in_range_with_memo(n - (first_digit_n * 10 ** prev_power_10), memo)
        result += first_digit_n * count_of_2_in_range_with_memo(10 ** prev_power_10 - 1, memo)
        if first_digit_n > 2:
            result += 10 ** prev_power_10
        elif first_digit_n == 2:
            result += n - (first_digit_n * 10 ** prev_power_10) + 1
        memo[n] = result
        return result

failed = []
i = 0
duration = 0
start_time = time.time()
memo = {}
while duration < 1:
    actual = count_of_2_in_range_with_memo(i, memo)
    expected = count_of_2_in_range_naive(i)
    duration = time.time() - start_time
    # print(f"{i} : {actual} (expected : {expected})")
    if actual != expected:
        failed.append(i)
    i += 1
print(f"failed : {failed} (over {i})")
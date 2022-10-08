import math
import random


def randN_from_rand5(N : int):
    N_FROM = 5
    while True:
        space_mult = 0
        current_space_size = N_FROM
        current_random = random.randint(0, N_FROM-1)
        while current_space_size < N:
            current_space_size *= N_FROM
            space_mult += 1
            current_random = current_random * N_FROM + random.randint(0, N_FROM-1)
        if current_random < (current_space_size // N * N):
            return current_random % N


result = [0] * 7
result_theo = [0] * 7
for i in range(7000):
    result[randN_from_rand5(7)] += 1
    result_theo[random.randint(0,6)] += 1
print(result)
print(result_theo)
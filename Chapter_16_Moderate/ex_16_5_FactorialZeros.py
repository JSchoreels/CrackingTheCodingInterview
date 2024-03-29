def factorial_zero(n):
    count_factor_5 = 0
    for i in range(n+1):
        rest = i
        while rest % 5 == 0 and rest > 0:
            rest //= 5
            count_factor_5 += 1
    return count_factor_5

for i in range(0,201):
    print(f"factorial_zero({i}):{factorial_zero(i)}")

assert factorial_zero(5) == factorial_zero(4) + 1
assert factorial_zero(25) == factorial_zero(24) + 2
assert factorial_zero(125) == factorial_zero(124) + 3
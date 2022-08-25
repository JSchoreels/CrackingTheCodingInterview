def triple_step(n):
    memo = [0] * (n + 1)
    if n <= 1: return 1
    elif n == 2: return 2
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    def triple_step(n):
        if memo[n] > 0:
            print(f"Using cache for n = {n}")
            return memo[n]
        else:
            print(f"Computing triple_step for n = {n}")
            result = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
            memo[n] = result
            return result
    return triple_step(n)

if __name__ == '__main__':
    assert triple_step(0) == 1
    assert triple_step(1) == 1
    assert triple_step(2) == 2
    assert triple_step(3) == 4
    assert triple_step(4) == 7
    print(triple_step(10))
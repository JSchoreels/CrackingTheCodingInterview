def parens(n):
    result = set()
    if n == 0:
        result.add('')
    else:
        rec_results = parens(n-1)
        result = set()
        for rec_result in rec_results:
            for i in range(len(rec_result)):
                if rec_result[i] == "(":
                    result.add(rec_result[:i+1]+'()'+rec_result[i+1:])
            result.add('()' + rec_result)
    return result

def parens_iter(n):
    result = set()
    buffer = [""] * n * 2
    def parens_iter(left_parens_left, right_parens_left, i):
        if i == n * 2:
            result.add(''.join(buffer))
        else:
            if left_parens_left > 0:
                buffer[i] = "("
                parens_iter(left_parens_left-1, right_parens_left, i+1)
            if right_parens_left > left_parens_left >= 0:
                buffer[i] = ")"
                parens_iter(left_parens_left, right_parens_left-1, i+1)
    parens_iter(n, n, 0)
    return result

print(parens(1))
print(parens(2))
print(parens(3))
print(parens(4))
print(parens_iter(1))
print(parens_iter(2))
print(parens_iter(3))
print(parens_iter(4))
assert parens(5) == parens_iter(5)
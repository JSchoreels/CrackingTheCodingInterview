def add_without_plus(x,y):
    sum = x ^ y
    carry = (x & y) << 1
    while carry != 0:
        old_sum = sum
        sum = old_sum ^ carry
        carry = (old_sum & carry) << 1
    return sum

for i in range(100):
    for j in range(100):
        assert add_without_plus(i,j) == i+j

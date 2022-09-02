# 8.11 Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

def coins(n, currencies = [25, 10, 5, 1]):
    currency = currencies[0]
    if currency == 1:
        return 1 # In this case, there is only one value to sum to n, n*1
    if n == 0:
        return 1 # In this case, it means that we can't remove anymore so the last call was already a "leaf" in the tree of possibilities
    total = 0
    while n >= 0:
        total += coins(n, currencies=currencies[1:]) # We can start at n with 0 currency taken
        n = n - currency
    return total

for i in range(100):
    print(f"For n={i}, coins(n)={coins(i)}")
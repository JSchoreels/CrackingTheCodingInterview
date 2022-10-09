import random


def random_subset(items, k):
    N = len(items)
    assert k <= N
    result = items[:k]
    for i in range(k, N):
        rand = random.randint(0, i)
        if rand < k:
            result[rand] = items[i]
    return result


results = {}
permutation_occurences = {}
for i in range(100000):
    input = [str(i) for i in range(10)]
    result = random_subset(input, 4)
    result.sort()
    perm_id = ','.join(result)
    permutation_occurences[perm_id] = permutation_occurences.get(perm_id, 0) + 1
    for item in result:
        results[item] = results.get(item, 0) + 1
occurences = list(results.items())
occurences.sort(key=lambda x : x[1])
print(occurences)
sorted_perm_occ = list(permutation_occurences.items())
sorted_perm_occ.sort(key=lambda x:x[1])
print(sorted_perm_occ)
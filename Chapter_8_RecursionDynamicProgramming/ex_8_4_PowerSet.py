# Power Set: Write a method to return all subsets of a set.

def subsets(set):
    if set == []:
        return []
    if len(set) == 1:
        return [set, []]
    subsets_of_subset = subsets(set[1:])
    result = subsets_of_subset.copy()
    for subset in subsets_of_subset:
        result.append([set[0]] + subset)
    return result

if __name__ == '__main__':
    l = subsets([1, 2, 3])
    l.sort(key = lambda x : f"{len(x)}.{''.join([str(i) for i in x])}")
    print(l)
    assert l == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

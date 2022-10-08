def pairs_with_sum(array, sum):
    first = 0
    last = len(array) - 1
    result = []
    array.sort()
    while (first < last):
        current_sum = array[first] + array[last]
        if current_sum == sum:
            result.append((array[first],array[last]))
            first += 1
            last -= 1
        elif current_sum < sum:
            first += 1
        else:
            last -= 1
    return result

print(pairs_with_sum([-5,-2,0,1,2, 3 ,4,5], 3))
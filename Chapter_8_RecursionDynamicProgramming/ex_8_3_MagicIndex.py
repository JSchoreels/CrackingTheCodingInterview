def magic_index_distinct(tab):
    if tab[0] > 0:
        return None
    if tab[-1] < len(tab)-1:
        return None
    def magic_index_distinct(start, end):
        mid_index = start + (end - start)//2
        print(f"searching between {start} and {end} with mid at {mid_index}")
        if tab[mid_index] == mid_index:
            return mid_index
        elif start == end:
            return None
        elif tab[mid_index] < mid_index:
            return magic_index_distinct(mid_index+1, end)
        elif tab[mid_index] > mid_index:
            return magic_index_distinct(start, mid_index-1)
    return magic_index_distinct(0, len(tab)-1)

def magix_index_duplicates(tab):
    def magix_index_duplicates(start, end):
        mid_index = start + (end - start)//2
        print(f"searching between {start} and {end} with mid at {mid_index}")
        result = []
        if tab[mid_index] == mid_index:
            result.append(mid_index)
        if start > end:
            return None
        right_search = magix_index_duplicates(max(tab[mid_index],mid_index+1), end)
        if right_search is not None:
            result.extend(right_search)
        left_search = magix_index_duplicates(start, min(mid_index-1, tab[mid_index]))
        if left_search is not None:
            result.extend(left_search)
        return result
    return magix_index_duplicates(0, len(tab)-1)

if __name__ == '__main__':
    tab = [-1, 2, 3, 4, 5, 6, 7]
    # tab should start with something <0 and end with something > size to "cross" f(i) = i since it is strictly increasing
    print(magic_index_distinct(tab))
    assert magic_index_distinct([-1, 1, 3, 4, 5, 6, 7]) == 1
    assert magic_index_distinct([-2, -1, 3, 4, 5, 6, 7]) is None
    duplicates = magix_index_duplicates([0, 1, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 12, 13])
    duplicates.sort()
    print(duplicates)

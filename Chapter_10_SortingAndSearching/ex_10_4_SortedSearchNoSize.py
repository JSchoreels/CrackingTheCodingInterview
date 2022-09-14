# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method. It does, however, have an elementAt ( i) method that returns the element at index i in
# 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.


def listy(l):
    return lambda i: l[i] if i < len(l) else -1

def get_size(listy):
    def search_end(start, end):
        if start == end:
            return start
        mid = start + (end - start)//2
        if listy(mid) >= 0:
            return search_end(mid+1, end)
        elif listy(mid) < 0:
            if listy(mid-1) < 0:
                return search_end(start, mid-1)
            else:
                return mid
    if listy(0) < 0:
        return 0
    i = 1
    while (listy(i) >= 0):
        i *= 2
    return search_end(i//2, i)

def search(listy, item):
    size = get_size(listy)
    def search(start, end):
        mid = start + (end-start)//2
        if listy(mid) == item:
            return mid
        elif listy(mid) > item:
            return search(start, mid-1)
        else:
            return search(mid+1, end)
    return search(0, size-1)

l = []
for i in range(20):
    l.append(i)
    size = get_size(listy(l))
    assert i+1 == size
    assert search(listy(l), 0) == 0
    assert search(listy(l), i//2) == i//2
    assert search(listy(l), i) == i

print(search(listy(l), 18))
# Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.

def sparse_search(l, item):
    def search(start, end):
        mid = start + (end - start) // 2
        if l[mid] == "":
            radius = 1
            while l[mid] == "":
                if mid+radius <= end and l[mid+radius] != "":
                    mid=mid+radius
                elif mid-radius >= start and l[mid-radius] != "":
                    mid=mid-radius
                if mid+radius > end and mid-radius < start:
                    return None
                radius += 1
        if l[mid] == item:
            return mid
        elif l[mid] > item:
            return search(start, mid-1)
        else:
            return search(mid+1, end)
    return search(0, len(l)-1)

l = ["a", "", "b", "", "", "", "c", "", ""]
print(sparse_search(l, "a"))
assert sparse_search(l, "a") == 0
print(sparse_search(l, "b"))
assert sparse_search(l, "b") == 2
print(sparse_search(l, "c"))
assert sparse_search(l, "c") == 6
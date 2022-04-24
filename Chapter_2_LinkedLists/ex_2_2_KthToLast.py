# Kth To Last
# Impplement an algorithm to find the kth to last element of a single linked list

from Chapter_2_LinkedLists.Node import Node, SortedList, SortedSet


def get_kth_to_last(linkedlist: Node, kth):
    size = 0
    node = linkedlist
    while node is not None:
        size += 1
        node = node.next
    i = 0
    kth_node = linkedlist
    while i < size - 1 - kth:
        kth_node = kth_node.next
        i += 1
    return kth_node.data


def get_kth_to_last_2(linkedlist: Node, kth):
    n1 = linkedlist
    n2 = linkedlist
    for i in range(kth):
        if n2 == None:
            raise ValueError("kth too big for list")
        n2 = n2.next
    while n2.next is not None:
        n1 = n1.next
        n2 = n2.next
    return n1.data

def get_kth_to_last_rec(linkedlist: Node, kth):

    def get_kth_to_last_rec_wrapper(linkedlist, kth):
        if linkedlist.next is None:
            if kth == 0:
                return (linkedlist.data, 0)
            else:
                return (None, 0)
        else:
            rec_call = get_kth_to_last_rec_wrapper(linkedlist.next, kth)
            if rec_call[1]+1 == kth:
                return linkedlist.data, rec_call[1]+1
            elif rec_call[0] is not None:
                return rec_call
            else:
                return None, rec_call[1] + 1

    return get_kth_to_last_rec_wrapper(linkedlist, kth)[0]

linkedlist = Node(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(get_kth_to_last_rec(linkedlist, 0))
print(get_kth_to_last_rec(linkedlist, 1))
print(get_kth_to_last_rec(linkedlist, 2))
print(get_kth_to_last_rec(linkedlist, 3))
print(get_kth_to_last_rec(linkedlist, 4))

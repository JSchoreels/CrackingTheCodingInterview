# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from Chapter_2_LinkedLists.Node import Node, LinkedList


def partition(list: LinkedList, x: int):
    lessers_head = None
    greaters_head = None
    lessers_tail = None
    greaters_tail = None
    n = list.head
    while n is not None:
        selected = n
        n = n.next
        selected.next = None
        if selected.data < x:
            lessers_head, lessers_tail = appendAndReturnNewHeadAndTail(lessers_head, lessers_tail, selected)
        else:
            greaters_head, greaters_tail = appendAndReturnNewHeadAndTail(greaters_head, greaters_tail, selected)
    if lessers_head is not None:
        list.head = lessers_head
        lessers_tail.next = greaters_head
    else:
        list.head = greaters_head

def appendAndReturnNewHeadAndTail(head, tail, selected):
    if head is None:
        head = selected
        tail = head
    else:
        tail.next = selected
        tail = selected
    return head, tail


if __name__ == "__main__":
    linked_list = LinkedList(1, 9, 1, 2, 7)
    partition(linked_list, 5)

    print(linked_list)
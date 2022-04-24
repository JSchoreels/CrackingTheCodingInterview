# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from Chapter_2_LinkedLists.Node import Node

llist = Node(9,1,2,7)

def partition(head: Node, x: int):
    n = head
    end = head
    while end.next is not None:
        end = end.next
    initial_end = end
    while n != initial_end:
        if n.next.data < x:
            n = n.next
        else:
            if n.next != initial_end:
                next = n.next
                n.next = n.next.next
                end.next = next
                end = end.next
                end.next = None

partition(llist,5)
print(llist)
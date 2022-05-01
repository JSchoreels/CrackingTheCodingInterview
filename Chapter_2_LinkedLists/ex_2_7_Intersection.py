# Given two (singly) linked lists determine if the two lists intersects. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked
# list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting

import unittest

from Chapter_2_LinkedLists.Node import LinkedList, Node


def intersection(l1: LinkedList, l2: LinkedList):
    # If l1 and l2 have an intersection, it means they have a shared end sublist of size k. The size of l1 and l2
    # are greater or equal than k. let say l1 is greater or equal than l2. It means if we start at size(l2)
    # from the end of l1, and we walk at the same pace through l1 and l2, the two pointers will meet at the intersection
    # point
    # First : determine if there is a common node at the end
    size_1, last_node_1 = get_size_and_last_node(l1)
    size_2, last_node_2 = get_size_and_last_node(l2)
    if last_node_1 is not last_node_2:
        return None
    if size_1 < size_2: # we want l1 bigger by simplicity
        l1, size_1, last_node_1,l2, size_2, last_node_2 = l2, size_2, last_node_2,l1, size_1, last_node_1
    n1 = l1.head
    n2 = l2.head
    for i in range(size_1 - size_2):
        n1 = n1.next
    while n1 is not n2:
        n1 = n1.next
        n2 = n2.next
    return n1


def get_size_and_last_node(l : LinkedList):
    if l.head is None:
        return 0, None
    size = 1
    n = l.head
    while n.next is not None:
        size += 1
        n = n.next
    return size, n


class TestStringMethods(unittest.TestCase):
    def test_intersection(self):
        input1_start1 = LinkedList(10, 11, 12)
        input1_start2 = LinkedList(20, 21, 22, 23)
        self.assertEqual(None, intersection(input1_start1, input1_start2))
        input1_end = Node(30, 31, 32)
        input1_start1.append(input1_end)
        input1_start2.append(input1_end)
        self.assertEqual(30, intersection(input1_start1, input1_start2).data)


if __name__ == '__main__':
    unittest.main()

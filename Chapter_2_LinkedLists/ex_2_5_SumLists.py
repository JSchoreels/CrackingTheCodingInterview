# Sum Lists : You have two numbers represented by a linked list, where each node contains a single digit. The digits
# are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two
# numbers and returne the sum as a linked list. (You are not allowed to "cheat" and just convert the linked list to an
# integer.)
import unittest
from Chapter_2_LinkedLists.Node import LinkedList, Node


def sum(l1 : LinkedList, l2 : LinkedList) -> LinkedList:
    size_l1 = l1.__sizeof__()
    size_l2 = l2.__sizeof__()
    if size_l1 < size_l2:
        l1, l2 = l2, l1
    carry = 0
    n1 = l1.head
    n2 = l2.head
    l_output = LinkedList()
    l_output_tail = None
    while n1 is not None or carry > 0:
        res_data = (n1.data if n1 else 0) + (n2.data if n2 else 0) + carry
        carry = res_data // 10
        new_output_node = Node(res_data % 10)
        if l_output.head is None:
            l_output.head = new_output_node
            l_output_tail = l_output.head
        else:
            l_output_tail.next = new_output_node
            l_output_tail = new_output_node
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None
    return l_output

class TestStringMethods(unittest.TestCase):
    def test_sum_samesize(self):
        self.assertEqual(LinkedList(2,1,9), sum(LinkedList(7, 1, 6), LinkedList(5,9,2)))
        self.assertEqual(LinkedList(8,1), sum(LinkedList(9), LinkedList(9)))

    def test_sum_different_size(self):
        self.assertEqual(LinkedList(2,1,9,1,1), sum(LinkedList(7,1,6,1,1), LinkedList(5,9,2)))
        self.assertEqual(LinkedList(8,2), sum(LinkedList(9,1), LinkedList(9)))
        self.assertEqual(LinkedList(8,0,1), sum(LinkedList(9,9), LinkedList(9)))
        self.assertEqual(LinkedList(2,1,9,1,1), sum(LinkedList(5,9,2), LinkedList(7,1,6,1,1)))
        self.assertEqual(LinkedList(8,2), sum(LinkedList(9), LinkedList(9,1)))
        self.assertEqual(LinkedList(8,0,1), sum(LinkedList(9), LinkedList(9,9)))

if __name__ == '__main__':
    unittest.main()
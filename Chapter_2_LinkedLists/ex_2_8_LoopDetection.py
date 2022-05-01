# Loop Detection : Given a linked list which might contain a loop, inplement an algorith; that returns the node
# at the beginning of the loop (if one exists)
import unittest
from Chapter_2_LinkedLists.Node import LinkedList, Node


def loop_detection(l : LinkedList):
    slow_walker = l.head
    fast_walker = l.head
    while fast_walker is not None and fast_walker.next is not None:
        fast_walker = fast_walker.next.next
        slow_walker = slow_walker.next
        if fast_walker is slow_walker: # collision at LOOP - k % LOOP (k with kth the start of the loop) because slow
            # did k step and fast has done k more, thus fast is at LOOP - k % LOOP from the start,
            # and he close distance 1 node at a time, thus slow will be at LOOP - k % 20 when collision happens
            break
    if fast_walker is None or fast_walker.next is None:
        return None
    slow_walker_2 = l.head
    while slow_walker is not slow_walker_2: # l.head is also at k element before the start of the loop by definition
        slow_walker = slow_walker.next
        slow_walker_2 = slow_walker_2.next
    return slow_walker


class TestStringMethods(unittest.TestCase):
    def test_loop_detection(self):
        k_first = LinkedList(1,2,3,4,5,6,7,8,9,10)
        self.assertEqual(None,loop_detection(k_first))
        loop_start = Node(10)
        loop = LinkedList(11, 12, 13, 14)
        k_first.append(loop_start)
        self.assertEqual(None,loop_detection(k_first))
        loop_start.next = loop.head
        loop.append(loop_start)
        self.assertEqual(10,loop_detection(k_first).data)

if __name__ == '__main__':
    unittest.main()

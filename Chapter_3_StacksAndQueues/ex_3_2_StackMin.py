# Stack Min : How would you design a stack which, in addition to push and pop, has a function min which
# returns the minimum element? Push, pop, min should all operation in O(1) time.
import unittest
from unittest import TestCase

from Chapter_3_StacksAndQueues.Stack import Node, Stack


class StackMin:

    def __init__(self):
        self.head: Node = None
        self.min_stack = Stack()

    def push(self, data):  # O(1)
        if self.min_stack.peek() is None or data <= self.min_stack.peek():
            self.min_stack.push(data)
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def peek(self):
        if self.head:
            return self.head.data

    def pop(self):
        if self.head:
            result = self.head.data
            if result == self.min_stack.peek():
                self.min_stack.pop()
            self.head = self.head.next
            return result

    def min(self):
        return self.min_stack.peek()


'''
PUSH 5 
5-x MIN=5
PUSH 2
2-5-x MIN=2,5
PUSH 4 
4-2-5-x MIN=2,5
PUSH 2 
2-4-2-5-x MIN=2,2,5
POP
4-2-5-x MIN=2,5
'''
class StackMinTest(TestCase):
    def test_stackmin(self):
        stackmin = StackMin()
        self.assertIsNone(stackmin.peek())
        self.assertIsNone(stackmin.min_stack.peek())
        self.assertIsNone(stackmin.head)
        stackmin.push(5)
        self.assertEqual(5, stackmin.min())
        stackmin.push(2)
        self.assertEqual(2, stackmin.min())
        stackmin.push(4)
        self.assertEqual(2, stackmin.min())
        stackmin.push(2)
        self.assertEqual(2, stackmin.min())
        stackmin.push(1)
        self.assertEqual(1, stackmin.min())
        stackmin.pop()
        self.assertEqual(2, stackmin.min())
        stackmin.pop()
        self.assertEqual(2, stackmin.min())
        stackmin.pop()
        self.assertEqual(2, stackmin.min())
        stackmin.pop()
        self.assertEqual(5, stackmin.min())
        stackmin.pop()
        self.assertIsNone(stackmin.peek())
        self.assertIsNone(stackmin.min_stack.peek())
        self.assertIsNone(stackmin.head)


if __name__ == '__main__':
    unittest.main()
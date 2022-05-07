# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

"""
PUSH 1
STACK None
REVST 1


PUSH 2
STACK 2
REVST 1

PUSH 3 4 5
STACK 5 4 3 2
REVST 1

POP
STACK 5 4 3 2
REVST None
RETURN 1

REVST NONE
STACK None
REVST 2 3 4 5
"""
import unittest

from Chapter_3_StacksAndQueues.Stack import Stack


class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.reversed_stack = Stack()

    def push(self, data):
        if self.reversed_stack.head is None:
            self.reversed_stack.push(data)
        else:
            self.stack.push(data)

    def pop(self):
        to_return = self.reversed_stack.pop()
        if self.reversed_stack.head is None:
            while self.stack.head is not None:
                self.reversed_stack.push(self.stack.pop())
        return to_return

    def peek(self):
        return self.reversed_stack.peek()

class MyQueueTest(unittest.TestCase):
    def test_myqueue(self):
        myqueue = MyQueue()
        myqueue.push(1)
        self.assertEqual(1,myqueue.peek())
        myqueue.push(2)
        myqueue.push(3)
        self.assertEqual(1,myqueue.pop())
        self.assertEqual(2,myqueue.pop())
        myqueue.push(4)
        myqueue.push(5)
        self.assertEqual(3,myqueue.pop())
        self.assertEqual(4,myqueue.pop())
        self.assertEqual(5,myqueue.pop())
        self.assertIsNone(myqueue.peek())
        self.assertIsNone(myqueue.stack.head)
        self.assertIsNone(myqueue.reversed_stack.head)

if __name__ == '__main__':
    unittest.main()
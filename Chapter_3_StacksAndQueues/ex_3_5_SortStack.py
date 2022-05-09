# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty
import unittest
from unittest import TestCase

from Chapter_3_StacksAndQueues.Stack import Stack

"""
3,5,2,4,1
expected output = 1,2,3,4,5

stack = 3,5,2,4,1
tmp = .

Reversing the stack in tmp to get room to work

stack = .
tmp = 1,4,2,5,3
 
Now we insert each element from tmp in stack in order

data = 1
stack = 1 # stopped because there is no bigger element metand we reached the end
tmp = 4,2,5,3

data = 4
stack = 1, 4 we pilled the element before we reached the end, and then we put it back in stack
tmp = 2,5,3

data = 2
stack = 1, 4 POP AND PUSH TO TMP (1,2,5,3)
stack = 4 Bigger met
stack = 2, 4 pushing data
stack = 


"""

def sort(stack : Stack):
    tmp_start = Stack()
    while stack.peek() is not None:
        tmp_start.push(stack.pop())
    # Now stack is empty and tmp is filled, we will insert each element, in stack in order
    while tmp_start.peek() is not None:
        current = tmp_start.pop()
        while stack.peek() is not None and stack.peek() < current:
            tmp_start.push(stack.pop()) # We remove and store in tmp everything that is smaller ( and already sorted )
        stack.push(current)
        while tmp_start.peek() is not None and tmp_start.peek() <= stack.peek():
            stack.push(tmp_start.pop())
    return stack


class Test(TestCase):
    def test(self):
        stack = Stack()
        stack.push(4)
        stack.push(5)
        stack.push(2)
        stack.push(1)
        stack.push(3)
        sort(stack)
        self.assertEqual("S[1 -> 2 -> 3 -> 4 -> 5 -> None]", stack.__repr__())

if __name__ == '__main__':
    unittest.main()
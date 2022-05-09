import unittest
from unittest import TestCase


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data} -> {self.next}"


class Stack:

    def __init__(self):
        self.head: Node = None

    def push(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def peek(self):
        return self.head.data if self.head else None

    def pop(self):
        value = self.peek()
        if self.head:
            self.head = self.head.next
        return value

    def __repr__(self):
        return f'S[{self.head}]'


class SortedStack:

    def __init__(self):
        self.sorted_stack = Stack()
        self.tmp_start = Stack()

    def push(self, data):
        if self.sorted_stack.peek() is None:
            self.sorted_stack.push(data)
        elif self.sorted_stack.peek() >= data:
            self.sorted_stack.push(data)
        else:
            while self.sorted_stack.peek() is not None and self.sorted_stack.peek() < data:
                self.tmp_start.push(self.sorted_stack.pop())
            self.sorted_stack.push(data)
            while self.tmp_start.peek() is not None:
                self.sorted_stack.push(self.tmp_start.pop())

    def __repr__(self):
        return f"{self.sorted_stack.__repr__()} (tmp: {self.tmp_start})"

    def pop(self):
        return self.sorted_stack.pop()

    def peek(self):
        return self.sorted_stack.peek()


def sort(stack: Stack):
    class Test(TestCase):
        def test(self):
            sortstack = SortedStack()
            sortstack.push(5)
            sortstack.push(6)
            sortstack.push(4)
            sortstack.push(7)
            sortstack.push(3)
            sortstack.push(9)
            sortstack.push(10)
            sortstack.push(2)
            sortstack.push(1)
            self.assertEqual("S[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 9 -> 10 -> None] (tmp: S[None])", sortstack.__repr__())

if __name__ == '__main__':
    unittest.main()
from __future__ import annotations


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def __repr__(self):
        return self.head.__repr__()


class Node:

    def __init__(self, data = None, *args):
        self.data = data
        self.next: Node = None
        n = self
        for node in args:
            extra_node = Node(node)
            n.next = extra_node
            n = n.next

    def __repr__(self):
        return f"{self.data} -> {self.next}"


class SortedList:

    def __init__(self, data=None, *args):
        self.data = data
        self.next: SortedList = None
        n = self
        for node in args:
            self.insert(node)

    def insert(self, data):
        n = self
        while n.next is not None and n.next.data < data:
            n = n.next
        new_node = SortedList(data)
        new_node.next = n.next
        n.next = new_node


class SortedSet(Node):

    def __init__(self, data = None, *args):
        self.data = data
        self.next: SortedList = None
        for node in args:
            self.insert(node)

    def insert(self, data):
        n = self
        if n.data != data:
            while n.next is not None and n.next.data < data:
                n = n.next
            if n.next is None or n.next.data != data:
                new_node = SortedSet(data)
                new_node.next = n.next
                n.next = new_node

from __future__ import annotations


class LinkedList:

    head: Node

    def __init__(self, *args):
        if len(args) != 0:
            self.head = Node(*args)
        else:
            self.head = None

    def insert_first(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def __repr__(self):
        return self.head.__repr__()

    def __eq__(self, other):
        return self.head == other.head

    def __sizeof__(self):
        return self.head.__sizeof__()


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

    def __eq__(self, other: Node):
        return other is not None and self.data == other.data and self.next == other.next

    def __sizeof__(self):
        size = 0
        n = self
        while n is not None:
            size += 1
            n = n.next
        return size

    def reverse(self) -> None:
        n = self.head
        prev = None
        while n is not None:
            n_next = n.next
            n.next = prev
            prev = n
            n = n_next
        self.head = prev


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

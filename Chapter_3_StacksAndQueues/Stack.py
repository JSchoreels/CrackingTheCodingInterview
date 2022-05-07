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

from Chapter_3_StacksAndQueues.Node import Node


class MyQueue:

    def __init__(self):
        self.head : Node = None
        self.tail : Node = None

    def queue(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        to_return = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return to_return.data

    def is_empty(self):
        return self.head is None and self.tail is None

    def peek(self):
        return self.head.data
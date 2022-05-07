# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
import unittest

from Chapter_3_StacksAndQueues.Stack import Stack


class WeightedStack(Stack):

    def __init__(self):
        super().__init__()
        self.weight = 0

    def push(self, weight):
        super().push(weight)
        self.weight += weight

    def peek(self):
        return super().peek()

    def pop(self):
        self.weight -= self.peek() if self.head is not None else 0
        return super().pop()

    def __repr__(self):
        return f"S[{self.head}](W:{self.weight})"


class SetOfStacks():

    def __init__(self, threshold):
        self.threshold : int = threshold
        self.stack_of_weightedstacks : WeightedStack = Stack()

    def push(self, data):
        current_stack = self.peek_stack()
        if current_stack is None or current_stack.weight >= self.threshold:
            new_stack = WeightedStack()
            new_stack.push(data)
            self.stack_of_weightedstacks.push(new_stack)
        else:
            current_stack.push(data)

    def peek(self) :
        self.peek_stack().peek()

    def peek_stack(self) -> WeightedStack:
        return self.stack_of_weightedstacks.peek()

    def pop(self):
        current_stack = self.peek_stack()
        if current_stack is not None:
            element_to_pop = current_stack.pop()
            if current_stack.peek() is None:
                self.stack_of_weightedstacks.pop()
            return element_to_pop

    def __repr__(self):
        return self.stack_of_weightedstacks.__repr__()

class StackOfPlatesTest(unittest.TestCase):
    def test_stackofplates(self):
        setofstacks = SetOfStacks(10)
        self.assertEqual('S[None]', setofstacks.__repr__())
        setofstacks.push(5)
        setofstacks.push(5)
        setofstacks.push(1)
        setofstacks.push(5)
        setofstacks.push(5)
        setofstacks.push(2)
        self.assertEqual('S[S[2 -> None](W:2) -> S[5 -> 5 -> 1 -> None](W:11) -> S[5 -> 5 -> None](W:10) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[S[5 -> 5 -> 1 -> None](W:11) -> S[5 -> 5 -> None](W:10) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[S[5 -> 1 -> None](W:6) -> S[5 -> 5 -> None](W:10) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[S[1 -> None](W:1) -> S[5 -> 5 -> None](W:10) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[S[5 -> 5 -> None](W:10) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[S[5 -> None](W:5) -> None]', setofstacks.__repr__())
        setofstacks.pop()
        self.assertEqual('S[None]', setofstacks.__repr__())

if __name__ == '__main__':
    unittest.main()
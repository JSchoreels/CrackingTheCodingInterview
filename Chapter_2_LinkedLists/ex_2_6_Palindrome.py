# Palindrome : Implement a function to check if a linked list is a palindrome
import unittest

from Chapter_2_LinkedLists.Node import LinkedList


def is_palindrome(l : LinkedList):
    l_size = size(l)
    prev = None
    n = l.head
    for i in range(l_size//2): # for 3//2=1 -> i in [0], 1->2->3 become x<-1|2->3. for 4//2=2 -> i in [0,1] so 1->2->3->4 become x<-1<-2|3->4
        n_next = n.next
        n.next = prev
        prev = n
        n = n_next
    if l_size % 2 == 0: # x<-1<-2|3->4. n = 3. prev = 2
        backward_runner = prev
        forward_runner = n
        prev = n
    else:
        backward_runner = prev # x<-1|2->3. n = 2. prev = 1
        forward_runner = n.next # 3
        prev = n
    is_palindrome = True
    while backward_runner is not None and forward_runner is not None:
        if is_palindrome and backward_runner.data != forward_runner.data:
            is_palindrome = False
        backward_runner_next = backward_runner.next # we will reset the order of the list as it was at the start
        backward_runner.next = prev
        prev = backward_runner
        backward_runner = backward_runner_next
        forward_runner = forward_runner.next # forward_runner just go forward
    return is_palindrome




def size(l : LinkedList) -> int:
    size = 0
    n = l.head
    while n is not None:
        size += 1
        n = n.next
    return size


class TestStringMethods(unittest.TestCase):
    def test_is_palindrome_even_size(self):
        self.assertTrue(is_palindrome(LinkedList(1,2,3,2,1)))
        self.assertTrue(is_palindrome(LinkedList(1,2,2,1)))
        self.assertTrue(is_palindrome(LinkedList(1,1)))
        self.assertTrue(is_palindrome(LinkedList(1)))
        self.assertFalse(is_palindrome(LinkedList(1,2,3)))
        self.assertFalse(is_palindrome(LinkedList(1,2,3,2,1,0)))

    def test_is_palindrome_no_mutation(self):
        input = LinkedList(1, 2, 3, 2, 1)
        is_palindrome(input)
        self.assertEqual(input, LinkedList(1, 2, 3, 2, 1))
        input = LinkedList(1, 2, 2, 1)
        is_palindrome(input)
        self.assertEqual(input, LinkedList(1, 2, 2, 1))


if __name__ == '__main__':
    unittest.main()

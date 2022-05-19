# 4.4
# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
import unittest
import math

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def check_balanced(tree: BinaryTree):
    def get_balance_and_height(current_tree: BinaryTree):
        if current_tree is None:
            return True,0
        left_balance, left_height = get_balance_and_height(current_tree.left)
        right_balance, right_height = get_balance_and_height(current_tree.right)
        is_balanced = left_balance and right_balance and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        return is_balanced, height
    return get_balance_and_height(tree)[0]


class TestCase(unittest.TestCase):
    def test(self):
        tree = minimal_tree(range(20))
        tree.to_graph().display()
        self.assertTrue(check_balanced(tree))
        tree.left.left.right = None
        self.assertFalse(check_balanced(tree))
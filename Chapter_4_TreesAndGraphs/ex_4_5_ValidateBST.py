# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree

# see code in class
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def validate_bst(tree: BinaryTree):
    return tree.is_sorted()

class TestCase(unittest.TestCase):
    def test(self):
       tree = minimal_tree(range(30))
       self.assertTrue(validate_bst(tree))
       tree.left.data = 31
       self.assertFalse(validate_bst(tree))

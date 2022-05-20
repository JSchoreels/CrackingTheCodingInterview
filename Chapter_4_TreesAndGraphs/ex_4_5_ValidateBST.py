# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree

# see code in class
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def validate_bst(tree: BinaryTree):
    if tree is None: return True
    return tree.is_bst()

class TestCase(unittest.TestCase):

    def test(self):
       tree = minimal_tree(range(30))
       self.assertTrue(validate_bst(tree))
       tree.left.data = 31
       self.assertFalse(validate_bst(tree))

    def test_trap(self):
       tree = BinaryTree(20)
       tree.left = BinaryTree(10)
       tree.left.right = BinaryTree(25)
       tree.left.left = BinaryTree(5)
       tree.right = BinaryTree(30)
       tree.to_graph().display()
       self.assertFalse(validate_bst(tree))


    def test_null(self):
       self.assertTrue(validate_bst(None))
       self.assertTrue(validate_bst(BinaryTree(2)))

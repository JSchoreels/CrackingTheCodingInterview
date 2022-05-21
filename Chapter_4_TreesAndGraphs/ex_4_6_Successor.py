# Ex 4.6 Successor: Write an algorithm to find the "next" node (i.e, in order successor) of a given node
# in a binary search tree. you may assume that each node has a link to its parent
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree


class BinaryTreeWithParent(BinaryTree):

    def __init__(self, data, parent):
        super().__init__(data)
        self.parent : BinaryTreeWithParent = parent

def minimal_tree_with_parent(array):
    def minimal_tree_with_parent(array, start, end, parent):
        if start == end:
            return BinaryTreeWithParent(array[start], parent)
        elif start > end:
            return None
        else:
            total_element = end - start + 1
            middle_element_index = start + total_element // 2
            tree = BinaryTreeWithParent(array[middle_element_index], parent)
            tree.left = minimal_tree_with_parent(array, start, middle_element_index-1, tree)
            tree.right = minimal_tree_with_parent(array, middle_element_index+1, end, tree)
            return tree
    return minimal_tree_with_parent(array, 0, len(array)-1, None)

def successor_in_order(tree : BinaryTreeWithParent):
    # left -> tree -> right.
    # If there is something at the right, it will recurse right -> left -> left -> ... -> left, until there is mothing at the left (even if at the right there is)
    n = tree
    if tree.right is not None:
        n = tree.right
        while n.left is not None:
            n = n.left
        return n
    else: # Now it means the in-order would backtrack until it can go to the right (when ascending), since all our direct parents are visited and their left also. so move up, then one to the right
        n = tree
        while n.parent is not None and n.parent.right == n:
            n = n.parent
        return n.parent if n.parent else None


class TestCase(unittest.TestCase):
    def testRightFarLeft(self):
        tree = minimal_tree_with_parent(range(20))
        tree.to_graph().display()
        self.assertEqual(6, successor_in_order(tree.left).data)
        self.assertEqual(10, successor_in_order(tree.left.right.right).data)
        self.assertEqual(None, successor_in_order(tree.right.right.right))


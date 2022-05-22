# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def first_common_ancestor(tree: BinaryTree, node_1: int, node_2: int) -> BinaryTree:
    def first_common_ancestor_rec(tree: BinaryTree, node_1: BinaryTree, node_2: BinaryTree):
        if tree is None:
            return None,False,False # Ancestor,LeftFound,RightFound
        left_ancestor = first_common_ancestor_rec(tree.left, node_1, node_2)
        if left_ancestor[0]:
            return left_ancestor
        right_ancestor = first_common_ancestor_rec(tree.right, node_1, node_2)
        if right_ancestor[0]:
            return right_ancestor
        node1_found = left_ancestor[1] or right_ancestor[1] or tree.data == node_1
        node2_found = left_ancestor[2] or right_ancestor[2] or tree.data == node_2
        if node1_found and node2_found:
            return tree,True,True
        else:
            return None,node1_found,node2_found
    return first_common_ancestor_rec(tree, node_1, node_2)[0]



class TestCase(unittest.TestCase):
    def test(self):
        tree = minimal_tree(range(20))
        tree.to_graph().display()
        self.assertEqual(5, first_common_ancestor(tree, 0, 6).data)
        self.assertEqual(10, first_common_ancestor(tree, 0, 10).data)
        self.assertEqual(2, first_common_ancestor(tree, 0, 3).data)
        self.assertEqual(15, first_common_ancestor(tree, 11, 16).data)
        self.assertEqual(None, first_common_ancestor(tree, 11, 30))

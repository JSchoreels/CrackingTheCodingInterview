# 4.3
# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
import unittest

from Chapter_4_TreesAndGraphs import BinaryTree
from Chapter_4_TreesAndGraphs.Node import Node
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def list_of_depths(tree: BinaryTree):
    list_by_depths = [None] * tree.height()

    def add_tree_to_list_by_depths(current_tree: BinaryTree, current_depth: int):
        if list_by_depths[current_depth] is None:
            list_by_depths[current_depth] = Node(current_tree.data)
        else:
            n = list_by_depths[current_depth]
            while n.next is not None:
                n = n.next
            n.next = Node(current_tree.data)
        if current_tree.left is not None:
            add_tree_to_list_by_depths(current_tree.left, current_depth + 1)
        if current_tree.right is not None:
            add_tree_to_list_by_depths(current_tree.right, current_depth + 1)
    add_tree_to_list_by_depths(tree, 0)
    return list_by_depths


class TestCase(unittest.TestCase):
    def test(self):
        tree = minimal_tree(range(20))
        self.assertEqual('[15 -> None, 7 -> 19 -> None, 3 -> 11 -> 17 -> None, 1 -> 5 -> 9 -> 13 -> 16 -> 18 -> None, 0 -> 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> None]',\
                         list_of_depths(tree).__repr__())
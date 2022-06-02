# 4.11
# Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
from __future__ import annotations

import unittest

from Chapter_4_TreesAndGraphs import BinaryTree
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


class BinarySearchTree(BinaryTree.BinaryTree):

    def __init__(self, data):
        self.left: BinarySearchTree = None
        self.right: BinarySearchTree = None
        self.data = data
        self.size = 1

    def insert(self, data):
        if data == self.data:
            raise ValueError("Duplicate Value")
        elif data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    def find(self, data):
        if data == self.data:
            return self
        elif data < self.data:
            return self.left.find(data) if self.left else None
        elif data > self.data:
            return self.right.find(data) if self.right else None

    def delete_node(self, data):
        if data < self.data:
            if self.left is None:
                raise ValueError("Element no found")
            self.left = self.left.delete_node(data)
            return self
        elif data > self.data:
            if self.right is None:
                raise ValueError("Element no found")
            self.right = self.right.delete_node(data)
            return self
        elif data == self.data:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_right = self.right
                if min_right.left is None:
                    self.data = self.right.data
                    self.right = self.right.delete_node(self.right.data)
                else:
                    while min_right.left.left is not None:
                        min_right = min_right.left
                    self.data = min_right.left.data
                    min_right.left = min_right.left.delete_node(min_right.left.data)
                return self


class TestCase(unittest.TestCase):
    def test(self):
        bst = BinarySearchTree(10)
        for elem in [5,2,8,1,4,7,9,15,13,18,12,14,17]:
            bst.insert(elem)
        bst.to_graph().display()
        bst.delete_node(13)
        bst.delete_node(18)
        bst.to_graph().display()

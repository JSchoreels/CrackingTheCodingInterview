# 4.11
# Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
from __future__ import annotations

import random
import unittest
from collections import defaultdict

from Chapter_4_TreesAndGraphs import BinaryTree
from Chapter_4_TreesAndGraphs.Graph import Graph


class BinarySearchTree(BinaryTree.BinaryTree):

    def __init__(self, data):
        self.left: BinarySearchTree = None
        self.right: BinarySearchTree = None
        self.data = data
        self.size = 1

    def insert(self, data):
        try:
            self.size += 1
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
        except ValueError:
            self.size -= 1
            raise

    def find(self, data):
        if data == self.data:
            return self
        elif data < self.data:
            return self.left.find(data) if self.left else None
        elif data > self.data:
            return self.right.find(data) if self.right else None

    def delete_node(self, data):
        self.size -= 1
        try:
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
        except:
            self.size += 1
            raise

    def get_random_node(self):
        selected_node = random.randint(0, self.size-1)
        def get_selected_node(tree : BinarySearchTree, selected_index : int):
            left_size = tree.left.size if tree.left else 0
            if selected_index < left_size :
                return get_selected_node(tree.left, selected_index)
            elif selected_index == left_size:
                return tree.data
            else:
                return get_selected_node(tree.right, selected_index - left_size - 1)
        return get_selected_node(self, selected_node)

    def to_graph(self) -> Graph:
        graph = Graph()
        def add_tree_to_graph(tree, graph):
            if tree.left is not None:
                graph.add_edges((f"{tree.data} ({tree.size})", f"{tree.left.data} ({tree.left.size})"))
                add_tree_to_graph(tree.left, graph)
            else:
                graph.add_edges((f"{tree.data} ({tree.size})", f"None.{tree.data}.L"))
            if tree.right is not None:
                graph.add_edges((f"{tree.data} ({tree.size})", f"{tree.right.data} ({tree.right.size})"))
                add_tree_to_graph(tree.right, graph)
            else:
                graph.add_edges((f"{tree.data} ({tree.size})", f"None.{tree.data}.R"))
            return graph
        return add_tree_to_graph(self, graph)



class TestCase(unittest.TestCase):
    def test(self):
        bst = BinarySearchTree(10)
        for elem in [5,2,8,1,4,7,9,15,13,18,12,14,17,17,17]:
            try:
                bst.insert(elem)
            except:
                print("Duplicate, ignoring")
        node_size = 900
        bst.to_graph().display(node_size=node_size)
        bst.delete_node(13)
        bst.to_graph().display(node_size=node_size)
        bst.delete_node(18)
        bst.to_graph().display(node_size=node_size)
        try:
            bst.delete_node(18)
        except:
            print("Not existing, ignoring")
        bst.to_graph().display(node_size=node_size)
        random_results = {}
        total_tries = 100000
        for i in range(total_tries):
            random_result = bst.get_random_node()
            random_results[random_result] = random_results.get(random_result, 0) + 1
        print(random_results)
        for result,count in random_results.items():
            self.assertAlmostEqual(count, total_tries/bst.size, delta=total_tries/bst.size/20.)
        for elem in [5,2,8,1,4,7,9,15,12,14,17]:
            self.assertIsNotNone(bst.find(elem))
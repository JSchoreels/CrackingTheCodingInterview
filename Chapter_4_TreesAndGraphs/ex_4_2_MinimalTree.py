# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.
import math
import unittest
from unittest import TestCase

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree

def minimal_tree_leftperfect(array):
    def minimal_tree(array, start, end):
        if start == end:
            return BinaryTree(array[start])
        elif start > end:
            return None
        else:
            total_element = end - start + 1
            middle_element_index = start + total_element // 2  # if 20 element, 10 is not a perfect 2^k-1, so we want 15.
            log2_middle = math.log2(middle_element_index - start + 1) # log2(10) = 3.xxx. We also need to take in account the start
            middle_element_index = 2**math.ceil(log2_middle)-1
            tree = BinaryTree(array[start + middle_element_index])
            tree.left = minimal_tree(array, start, start + middle_element_index-1)
            tree.right = minimal_tree(array, start + middle_element_index+1, end)
            return tree
    return minimal_tree(array, 0, len(array)-1)

def minimal_tree(array):
    def minimal_tree(array, start, end):
        if start == end:
            return BinaryTree(array[start])
        elif start > end:
            return None
        else:
            total_element = end - start + 1
            middle_element_index = start + total_element // 2
            tree = BinaryTree(array[middle_element_index])
            tree.left = minimal_tree(array, start, middle_element_index-1)
            tree.right = minimal_tree(array, middle_element_index+1, end)
            return tree
    return minimal_tree(array, 0, len(array)-1)

def minimal_tree_perfect(array):
    current_level = [BinaryTree(array[0])]
    parent_level = []
    while len(current_level) > 0 :
        current_tree = current_level.pop(0)
        parent_level.append(current_tree)
        current_tree



class TreeTestCase(TestCase):
    def test(self):
        tab = [i for i in range(20)]
        tree = minimal_tree(tab)
        graph = tree.to_graph()
        graph.display(draw_func=lambda x : x.draw)
        self.assertEqual(5, tree.height())
        self.assertTrue(tree.is_sorted())

if __name__ == '__main__':
    unittest.main()
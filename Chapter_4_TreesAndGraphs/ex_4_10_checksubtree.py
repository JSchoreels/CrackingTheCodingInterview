# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def find(t1: BinaryTree, t2_root_data: int):
    if t1 is None:
        return None
    elif t1.data == t2_root_data:
        return t1
    find_left = find(t1.left, t2_root_data)
    if find_left is not None:
        return find_left
    find_right = find_left
    if find_right is not None:
        return find_right
    return None


def equals_tree(root_candidate: BinaryTree, t2: BinaryTree):
    if root_candidate is None and t2 is None:
        return True
    elif root_candidate is None and t2 is not None or root_candidate is not None and t2 is None:
        return False
    else:
      return root_candidate.data == t2.data and equals_tree(root_candidate.left, t2.left) and equals_tree(root_candidate.right, t2.right)


def subtree(t1: BinaryTree, t2: BinaryTree):
    if t2 is None:
        return True
    t2_root_data = t2.data
    root_candidate = find(t1, t2_root_data)
    if root_candidate:
        return equals_tree(root_candidate, t2)
    else:
        return False


class TestCase(unittest.TestCase):
    def test(self):
        t1 = minimal_tree(range(20))
        t2 = t1.left.left
        t1.to_graph().display()
        self.assertTrue(subtree(t1, t2))
        self.assertFalse(subtree(t2, t1))
        self.assertTrue(subtree(t1, None))
        self.assertFalse(subtree(t1, BinaryTree(21)))
        self.assertFalse(subtree(t1, BinaryTree(10)))
        self.assertTrue(subtree(t1, BinaryTree(0)))
# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree
from Chapter_4_TreesAndGraphs.ex_4_2_MinimalTree import minimal_tree


def zip_permutations(left_sequence: list[int], rigt_sequence: list[int]):
    def zip_permutations_rec(left_to_add : list[int]) -> (list[list[int]], int):
        if not left_to_add:
            return [(left_sequence,len(left_sequence))]  # permutations, last_index_of_right
        else:
            to_add = left_to_add.pop(0)
            new_result = []
            previous_permutations = zip_permutations_rec(left_to_add)
            for permutation, last_index_of_right in previous_permutations:
                for i in range(0, last_index_of_right+1):
                    new_permutation = permutation.copy()
                    new_permutation.insert(i, to_add)
                    new_result.append((new_permutation,i))
            return new_result
    return list(map(lambda x:x[0], zip_permutations_rec(rigt_sequence.copy())))




def bst_sequences(tree: BinaryTree):
    assert tree is None or tree.is_bst()
    if tree is None:
        return None
    else:
        if not tree.left and not tree.right:
            return [[tree.data]]
        if not tree.left:
            result = []
            for seq in bst_sequences(tree.right):
                new_seq = [tree.data] + seq
                result.append(new_seq)
            return result
        if not tree.right:
            result = []
            for seq in bst_sequences(tree.left):
                new_seq = [tree.data] + seq
                result.append(new_seq)
            return result
        sequences = []
        for left_seq in bst_sequences(tree.left):
            for right_seq in bst_sequences(tree.right):
                suffix_seqs = zip_permutations(left_seq, right_seq)
                for suffix_seq in suffix_seqs:
                    new_tree_seq = [tree.data] + suffix_seq
                    sequences.append(new_tree_seq)
        return sequences


class TestCase(unittest.TestCase):
    def test_book(self):
        tree = BinaryTree(2)
        tree.left = BinaryTree(1)
        tree.right = BinaryTree(3)
        self.assertEqual("[[2, 3, 1], [2, 1, 3]]", bst_sequences(tree).__repr__())


    def test_book2(self):
        tree = BinaryTree(2)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(0)
        tree.right = BinaryTree(3)
        tree.right.right = BinaryTree(5)
        result = bst_sequences(tree).__repr__()
        print(result)
        self.assertEqual("[[2, 3, 5, 1, 0], [2, 3, 1, 5, 0], [2, 1, 3, 5, 0], [2, 3, 1, 0, 5], [2, 1, 3, 0, 5], [2, 1, 0, 3, 5]]",
                         result)

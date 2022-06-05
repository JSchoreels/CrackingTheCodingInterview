# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes)
import unittest

from Chapter_4_TreesAndGraphs.BinaryTree import BinaryTree


def paths_with_sum(tree : BinaryTree, sum : int):
    cumulative_values = {}
    def paths_with_sun_with_base(tree : BinaryTree, base: int):
        if tree is None:
            return 0
        else:
            current_cumulative_value = base + tree.data
            cumulative_values[current_cumulative_value] = cumulative_values.get(current_cumulative_value, 0) + 1
            count = 0
            if current_cumulative_value == sum:
                count += 1
            count += cumulative_values.get(current_cumulative_value-sum, 0)
            count_left = paths_with_sun_with_base(tree.left, current_cumulative_value)
            count_right = paths_with_sun_with_base(tree.right, current_cumulative_value)
            print(f"{tree.data} {current_cumulative_value} {cumulative_values} C:{count} L:{count_left} R:{count_right}")
            cumulative_values[current_cumulative_value] = cumulative_values.get(current_cumulative_value, 0) - 1
            return count + count_left + count_right
    return paths_with_sun_with_base(tree, 0)


class TestCase(unittest.TestCase):
    def test(self):
        tree = BinaryTree(5)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(4)
        tree.left.left.right = BinaryTree(10)
        tree.right = BinaryTree(-1)
        tree.right.right = BinaryTree(1)
        tree.right.right.right = BinaryTree(5)
        tree.right.right.right.left = BinaryTree(1)
        tree.right.right.right.right = BinaryTree(5)
        self.assertEqual(5,paths_with_sum(tree, 10))
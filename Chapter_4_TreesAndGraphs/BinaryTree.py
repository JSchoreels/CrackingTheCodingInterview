from Chapter_4_TreesAndGraphs.Graph import Graph


class BinaryTree:

    def __init__(self, data):
        self.left : BinaryTree = None
        self.right : BinaryTree = None
        self.data = data

    def to_graph(self) -> Graph:
        graph = Graph()
        def add_tree_to_graph(tree, graph):
            if tree.left is not None:
                graph.add_edges((tree.data, tree.left.data))
                add_tree_to_graph(tree.left, graph)
            else:
                graph.add_edges((tree.data, f"None.{tree.data}.L"))
            if tree.right is not None:
                graph.add_edges((tree.data, tree.right.data))
                add_tree_to_graph(tree.right, graph)
            else:
                graph.add_edges((tree.data, f"None.{tree.data}.R"))
            return graph
        return add_tree_to_graph(self, graph)

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def is_bst(self):
        def is_bst_and_get_minmax(tree: BinaryTree):
            if tree is None:
                return True, None, None
            else:
                left_valid, left_min, left_max = is_bst_and_get_minmax(tree.left)
                if not left_valid:
                    return False, None, None
                right_valid, right_min, right_max = is_bst_and_get_minmax(tree.right)
                if not right_valid:
                    return False, None, None
                if (left_max is None or left_max < tree.data) and (right_min is None or right_min > tree.data):
                    return True, left_min if left_min else tree.data, right_max if right_max else tree.data
                else:
                    return False, None, None
        return is_bst_and_get_minmax(self)[0]
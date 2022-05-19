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
            if tree.right is not None:
                graph.add_edges((tree.data, tree.right.data))
                add_tree_to_graph(tree.right, graph)
            return graph
        return add_tree_to_graph(self, graph)

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def is_sorted(self):
        left_sorted = self.left.is_sorted() and self.left.data < self.data if self.left else True
        right_sorted = self.right.is_sorted() and self.right.data > self.data if self.right else True
        return left_sorted and right_sorted
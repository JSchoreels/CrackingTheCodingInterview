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

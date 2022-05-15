# 4.1 Route Between Nodes: Given a directed graph and two nodes (S and E), design an algorithm to
# find out whether there is a route from S to E.

import unittest
from queue import Queue

from Chapter_4_TreesAndGraphs.Graph import Graph

def route(graph: Graph, S, E):
    graph.reset_markings()
    queue = Queue()
    [ queue.put((S, dest)) for dest in graph.edges[S].keys() ]
    while not queue.empty():
        src, current_node = queue.get()
        if not graph.nodes[current_node].get('visited'):
            graph.mark_visited((src, current_node))
            graph.mark_visited(current_node)
            if current_node == E:
                graph.mark_matched(E)
                return True
            else:
                [queue.put((current_node, dest)) for dest in graph.edges.get(current_node, {}).keys() if not graph.nodes[dest].get('visited')]
    return False

class TestCase(unittest.TestCase):
    def test(self):
        graph = Graph().add_edges((1, 2), (3, 4), (2, 4), (5,4), (1,5), (4,1), (5,6), (1,6), (2,7))
        route(graph, 1,4)
        graph.display()


if __name__ == '__main__':
    unittest.main()
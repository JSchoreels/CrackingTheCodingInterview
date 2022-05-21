# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
import unittest
import time
import random
from functools import reduce
import matplotlib.pyplot as plt

from Graph import Graph

def has_cycle(graph, elt, path):
    if graph.nodes[elt].get('matched'):
        return False
    if graph.nodes[elt].get('visited'):
        return True
    for nxt in graph.edges.get(elt, {}).keys():
        graph.mark_visited(elt)
        plt.pause(.01)
        graph.display()
        if has_cycle(graph, nxt, path):
            return True
    path.insert(0, elt)
    graph.mark_matched(elt)
    plt.pause(.01)
    graph.display()
    print(path)
    return False

def build_order(projects : list, dependencies: list[tuple]):
    graph = Graph()
    graph.add_nodes(*projects).add_edges(*dependencies)
    # graph.display()
    path = []
    for node in graph.nodes:
        if graph.nodes[node].get('matched'):
            continue
        else:
            if has_cycle(graph, node, path):
                raise ValueError("Dependencies has a loop, can't find an order")
    print(path)


class UnitTest(unittest.TestCase):
    def test(self):
        projects = []
        deps = []
        for i in range(6):
            for j in range(6):
                start = random.randint(i*5, (i+1)*5)
                end = random.randint((i+1)*5+1, (i+2)*5)
                deps.append((start, end))
        build_order(projects, deps)
        input("")


if __name__ == '__main__':
    plt.ion()
    unittest.main()

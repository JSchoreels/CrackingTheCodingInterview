import matplotlib
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


class Graph:

    def __init__(self):
        self.nodes: map = {}
        self.edges: map = {}
        self.reversed_edges: map = {}


    def add_nodes(self, *nodes):
        for node in nodes:
            self.nodes[node] = {}
            if node not in self.edges:
                self.edges[node] = {}
        return self

    def add_edges(self, *edges):
        for edge in edges:
            source = edge[0]
            dest = edge[1]
            edge_metadata = {}
            self.nodes[source] = {}
            if source not in self.edges:
                self.edges[source] = {}
            self.edges[source][dest] = edge_metadata
            self.nodes[dest] = {}
            if dest not in self.reversed_edges:
                self.reversed_edges[dest] = {}
            self.reversed_edges[dest][source] = edge_metadata
        return self

    def mark_visited(self, elt):
        self.mark(elt, 'visited', mark_origin_of_edge=True)

    def mark_matched(self, elt):
        self.mark(elt, 'matched', mark_origin_of_edge=True)

    def mark(self, elt, status, mark_origin_of_edge=True):
        if isinstance(elt, int):
            self.nodes[elt][status] = True
        if isinstance(elt, tuple):
            source = elt[0]
            dest = elt[1]
            self.edges[source][dest][status] = True
            if mark_origin_of_edge:
                self.nodes[source][status] = True

    def display(self, draw_func = lambda g: g.draw, node_size=300):
        plt.clf()
        graph = nx.DiGraph(self.edges)
        pos = graphviz_layout(graph, prog="dot")
        nodes = [node for node in self.nodes if "None" not in str(node)]
        labels = {id: id for id in nodes}
        draw_func(nx)(graph,pos, nodelist=nodes, node_size=node_size, font_size=9, labels=labels, node_color="tab:blue", font_color="whitesmoke")
        for color, status in [('tab:red', 'visited'),('tab:green','matched')]:
            nodes = [node for node in self.nodes if self.nodes[node].get(status)]
            edges = [ (src,dest) for src in self.edges.keys() for dest in self.edges[src].keys() if self.edges[src][dest].get(status, False)]
            draw_func(nx)(graph, pos, nodelist=nodes, node_size=node_size, font_size=9, edgelist=edges, labels=labels, width=4, edge_color=color, node_color=color, font_color="whitesmoke")
        plt.show()


    def reset_status(self, status):
        for node in self.nodes:
            if self.nodes[node].get(status):
                self.nodes[node][status] = False
        for src in self.edges:
            for dest in self.edges[src]:
                if self.edges[src][dest].get(status):
                    self.edges[src][dest][status] = False

    def reset_markings(self):
        for status in ['visited', 'matched']:
            self.reset_status(status)
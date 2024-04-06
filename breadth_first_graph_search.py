from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
 
    def add_edge(self, vertice_01, vertice_02):
        """
        Function to add an edge to the graph, i.e. add an vertice_02 to the
        adjacency list of given vertice_01
        """
        self.adjacency_list[vertice_01].append[vertice_02]

    
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, root_x, root_y):
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(self):
    minimum_spanning_tree = []
    index, edges = 0, 0

    sorted_edges = sorted(self.graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(self.V):
        parent.append(node)
        rank.append(0)

    while edges < self.V - 1:
        source, destination, weight = sorted_edges[index]
        index += 1

        root_source = self.find(parent, source)
        root_destination = self.find(parent, destination)

        if root_source != root_destination:
            edges += 1
            minimum_spanning_tree.append([source, destination, weight])
            self.union(parent, rank, root_source, root_destination)

    print("Edges of the minimum spanning tree")
    for source, destination, weight in minimum_spanning_tree:
        print("%d - %d: %d" % (source, destination, weight))
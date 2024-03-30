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
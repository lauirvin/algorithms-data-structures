# Week 7 Lab

# 1. Implement an unweighted and undirected graph data structure in the programming language of your choice, where the nodes consist of positive integers. You can either use an adjacency matrix or an adjacency list approach. You must use Object Oriented Programming for this task.


class Graph:
    def __init__(self):
        self.graphDict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []
            return("Vertex created")

    def add_directed_edge(self, v1, v2):
        if v1 in self.graphDict:
            self.graphDict[v1] = []
            self.graphDict[v1].append(v2)   
        if v2 in self.graphDict:
            self.graphDict[v2] = []
            self.graphDict[v2].append(v1)         
    
    def add_undirected_edge(self, v1, v2):
        self.add_directed_edge(v1, v2)
        self.add_directed_edge(v2, v1)

    def display(self):
        return self.graphDict


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_directed_edge("a", "b")
    g.add_directed_edge("a", "e")
    g.add_directed_edge("a", "c")
    g.add_directed_edge("b", "e")
    g.add_directed_edge("b", "d")
    print(g.display())
# 1. Implement an unweighted and undirected graph data structure in the programming language of your choice, where the nodes consist of positive integers. You can either use an adjacency matrix or an adjacency list approach. You must use Object Oriented Programming for this task.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class vertex(object):
    def __init__(self, label, edges=[]):
        self.label = label
        self.edges = []


class Graph:
    def __init__(self):
        self.graphDict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

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

# 2. Implement either the BFS or DFS graph traversal (you can use the pseudocode in the lecture slides to help). Save the nodes traversed in a text file, entitled either DFS.txt or BFS.txt, depending on which traversal you end up implementing.

    def depth_first_search(self, start_node):
        s = Stack()
        visited = []
        s.push(start_node)
        while s.empty() == False:
            u = s.pop()
            if u not in visited:
                visited.append(u)
                for e in self.graphDict[u]:
                    s.push(e)
        f = open('DFS.txt', 'w')
        f.write(str(visited))
        f.close

        return visited

# 3. Implement a function called isPath(v,w), where v∈V and w∈V (V is the set of all nodes in the graph) to check if there is a path between the two given nodes v and w.

    def isPath(self, start_node, end_node):
        all_nodes = self.depth_first_search(start_node)
        if start_node and end_node in all_nodes:
            return True
        else:
            return False

# Week 8 Lab

    def dijkstra(self, source, desintation):
        v = source
        for n in self.graphDict:
            n.tw = float('inf')
        source.tw = 0
        visited = []
        while v != destination:
            for u in v.edges:
                if v.tw + v[u].w < u.tw:
                    u.tw = v.tw + v[u].w
                    u.pre = v
                visited.append(v)
                minimum = float('inf')
                for n in v:
                    if n not in visited and n.tw < minimum:
                        v = n
                        minimum = n.tw


if __name__ == "__main__":
    vertex1 = "1"
    vertex2 = "2"
    vertex3 = "3"
    vertex4 = "4"
    vertex5 = "5"
    g = Graph()
    g.add_vertex(vertex1)
    g.add_vertex(vertex2)
    g.add_vertex(vertex3)
    g.add_vertex(vertex4)
    g.add_vertex(vertex5)
    g.add_directed_edge(vertex1, vertex2)
    g.add_directed_edge(vertex1, vertex5)
    g.add_directed_edge(vertex1, vertex3)
    g.add_directed_edge(vertex2, vertex5)
    g.add_directed_edge(vertex2, vertex4)
    print(g.display())
    g.dijkstra(vertex3, vertex5)

    # print(g.depth_first_search("1"))
    # print(g.isPath("1","3"))
    # print(g.isPath("1","4"))

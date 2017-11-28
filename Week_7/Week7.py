# Week 7 Lab

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


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("1")
    g.add_vertex("2")
    g.add_vertex("3")
    g.add_vertex("4")
    g.add_vertex("5")
    g.add_directed_edge("1", "2")
    g.add_directed_edge("1", "5")
    g.add_directed_edge("1", "3")
    g.add_directed_edge("2", "5")
    g.add_directed_edge("2", "4")

    print(g.display())
    print(g.depth_first_search("1"))
    print(g.isPath("1","3"))
    print(g.isPath("1","4"))

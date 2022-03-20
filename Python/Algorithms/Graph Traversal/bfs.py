from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def setEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        # Initialize a queue and a set
        visited = set()
        queue = []

        # Enqueue intial node to the queue
        queue.append(s)

        # Mark enqueued node as visited
        visited.add(s)

        # Begin a loop that will go on as long as the queue is not empty
        while queue:
            # Dequeue the node from the front of the queue, and save it to a variable u
            u = queue.pop(0)
            print(u, end=" ")

            # Loop over the neighbours of u that are not visited
            for v in self.graph[u]:
                if v not in visited:
                    # Enqueue the current neighbour to the queue and mark it as visited
                    queue.append(v)
                    visited.add(v)

g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)

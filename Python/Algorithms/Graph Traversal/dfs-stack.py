from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        # Initialize a stack and a set
        visited = set()
        st = []
        # Push the initial node onto the stack
        st.append(startNode)

        # Start a loop that will go on as long as the stack is not empty
        while(len(st)):
            # Pop the last node in the stack, and remove it from the stack
            cur = st[-1]
            st.pop()

            # If current node is not visited, add it to visited set
            if(cur not in visited):
                print(cur, end=" ")
                visited.add(cur)

            # Loop over the neighbours of the currnet node that have not yet been visited,
            # and push the unvisited nodes onto the stack
            for vertex in self.graph[cur]:
                if(vertex not in visited):
                    st.append(vertex)

"""
Time complexity: O(V + E)

where V = vertices (nodes) and E = Edges
"""

g = Graph()
g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.DFS(2)
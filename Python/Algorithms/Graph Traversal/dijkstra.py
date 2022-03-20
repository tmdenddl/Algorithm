
"""
Dijkstra Algorithm is used to find the shortest path between 2 nodes in a graph.
It gives the minimum distance between a starting node and every other node in the graph.

Steps:
1. Set nodes' distance to infinity except the source node which will have distance 0
2. Push the source node in a min_priority quque in the form of <distance, node>
3. Pop the node with the minimum distance from the queue (at first that node is the source)
4. Update the distance of the neighbour nodes to the popped node in case of 
   "(current node distance + edge weight) < neighbour node distance", then push the vertex
5. If the popped node is visited before, continue without using it
6. Apply the same algorithm again until the priority queue is empty

Walkthrough:
1. Visit the unvisited node with the smallest known distance. Initially, that's the start node itself.
2. From the current node, check the distance to it's unvisited neighbours.
3. From the current node, calculate the distance of each neighbour from the start node.
4. If the calculated distance of a neighbour node is less than the known shortest distance to it, update the shortest distance to the node
5. Update the previous node, and set the current node as visited.
6. Repeat from step 1 to 5 until we've visited all the nodes.

Time Complexity: O(|E|log|V|)
"""
####################################################################################
"""
Network delay time - Medium #743

There are N network nodes, laballed 1 to N. 
Given times, a list of travel times as directed edges times[i] = (u, v, w).
- u is the source node
- v is the target node
- w is the time/distance/cost it takes for a signal to travel form a source to the target

We'll send a signal from a certain node K. How long will it take for all the nodes to receive the signal?
If it's impossible, simply return -1.


Example:

Input: 
times = [
    [2, 1, 1],  # From node 2 to node 1, it costs 1
    [2, 3, 1],  # From node 2 to node 3, it costs 1
    [3, 4, 1]   # From node 3 to node 4, it costs 1
]
N = 4,  # Number of the total nodes
K = 2   # We'll start from the node K (node 2)

Output: 2
"""

from collections import defaultdict
from typing import List
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Initialize the graph container with the dictionary and the list 
        # key -> shortest distance to the node from the start node
        # value -> node
        g = defaultdict(list)
        # u = start node
        # v = end node
        # cost = distance
        for u, v, cost in times:
            g[u].append((cost, v))

        # Initialize a min_heap and a set
        # min_heap will be used to keep track of the distance to the node from the starting node and the node
        min_heap = [(0, K)]
        visited = set()

        # Set nodes' distance to infinity except the source node which will have distance 0
        distance = {i: float('inf') for i in range(1, N+1)}
        # Set K as the start node, and distance to itself is 0
        distance[K] = 0

        while min_heap:
            # Get the node with the smallest distance
            # cur_dist indicates the currently known distance to the node u from the start node
            # u indicates the target node
            cur_dist, u = heappop(min_heap)
            # If node u is already visited, skip
            if u in visited:
                continue
            # else add node u to the list of visted nodes
            visited.add(u)

            # If we've visited all the nodes, return the current distance
            if len(visited) == N:
                return cur_dist

            # Else, loop through the list
            for direct_distance, v in g[u]:
                # If the current distance from the start node to the previous node + the direct distance from the previous to the current node 
                # is smaller than the currently known shrotest distance, replace the distance and update the heap
                if cur_dist + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_distance
                    heappush(min_heap, (cur_dist + direct_distance, v))
        return -1

"""
Network Delay Time - Medium #743

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target,
how long will it take for all nodes to receive the signal? If impossible, return -1
K = starting node
N = number of nodes


Example:

Input: 
[
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]
N = 4, K = 2

Output:
2

"""
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list)

        for u, v, cost in times:
            g[u].append((cost, v))

        min_heap = [(0, K)]

        visited = set()

        distance = {i:float('inf') for i in range(1, N+1)}

        distance[K] = 0

        while min_heap:
            cur_distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == N:
                return cur_distance
            
            for direct_distance, v in g[u]:
                if cur_distance + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

            return -1
    
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""
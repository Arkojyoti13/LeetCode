from queue import PriorityQueue
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = defaultdict(list)

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t)) 
        queue = [(passingFees[0], 0, 0)]
        dist = [float('inf') for i in range(n)]
        while queue:
            cost, time, city = heappop(queue)
            
            if city == n - 1:
                return cost
            
            for neigh, t in graph[city]:
                new_time = time + t
                if (dist[neigh] > t+time) and (new_time <= maxTime):
                    heappush(queue, (cost + passingFees[neigh], new_time, neigh))
                    dist[neigh] = new_time
                    
        return -1
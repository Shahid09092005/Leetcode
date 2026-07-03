from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        # Build adjacency list
        graph = defaultdict(list)
        costs = []

        for u, v, cost in edges:
            graph[u].append((v, cost))
            costs.append(cost)

        n = len(online)
        costs = sorted(set(costs))      # unique edge costs

        # Check if a minimum edge cost = threshold is possible
        def can(threshold):

            @lru_cache(None)
            def dfs(node):

                # Reached destination
                if node == n - 1:
                    return 0

                # Intermediate node is offline
                if node != 0 and not online[node]:
                    return float('inf')

                ans = float('inf')

                for nxt, cost in graph[node]:

                    # Edge doesn't satisfy threshold
                    if cost < threshold:
                        continue

                    # Intermediate offline node
                    if nxt != n - 1 and not online[nxt]:
                        continue

                    ans = min(ans, cost + dfs(nxt))

                return ans

            return dfs(0) <= k

        # Binary Search
        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if can(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans
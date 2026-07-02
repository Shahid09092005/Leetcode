class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # starting health after first cell
        health -= grid[0][0]
        if health < 1:
            return False

        # best health seen at each cell
        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        q = deque([(0, 0, health)])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, h = q.popleft()

            if (x, y) == (m - 1, n - 1):
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]

                    if nh < 1:
                        continue

                    if nh <= best[nx][ny]:
                        continue

                    best[nx][ny] = nh
                    q.append((nx, ny, nh))

        return False
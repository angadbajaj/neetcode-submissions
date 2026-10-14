class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            directions = [1,0], [-1,0], [0,-1], [0,1]
            area = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c+dc) in range(cols) and (r+dr,c+dc) not in visited and grid[r+dr][c+dc] == 1:
                        visited.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea
        
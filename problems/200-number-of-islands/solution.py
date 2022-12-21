from collections import deque


class Solution:
    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ]

    def breadth_first_search(self, r: int, c: int):
        q = deque()
        p = (r, c)
        self.visited.add(p)
        q.append(p)
        while q:
            # popleft for bfs
            # pop for dfs
            row, col = q.popleft()

            for dr, dc in self.directions:
                r = row + dr
                c = col + dc
                point = (r, c)
                if (
                    r in range(self.rows)
                    and c in range(self.cols)
                    and self.grid[r][c] == "1"
                    and point not in self.visited
                ):
                    q.append(point)
                    self.visited.add(point)

    # noinspection PyAttributeOutsideInit
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        islands = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.breadth_first_search(row, col)
                    islands += 1

        return islands

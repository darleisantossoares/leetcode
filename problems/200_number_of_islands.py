class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cnt = 0

        visited = set()

        def get_neighbors(i, j):

            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for neighbor in neighbors:

                new_i, new_j = i + neighbor[0], j + neighbor[1]

                # out of bounds
                if new_i < 0 or new_i >= len(grid):
                    continue

                if new_j < 0 or new_j >= len(grid[0]):
                    continue

                # already has been visited
                if (new_i, new_j) in visited:
                    continue

                visited.add((new_i, new_j))

                if grid[new_i][new_j] == "1":
                    get_neighbors(new_i, new_j)


        for i, row in enumerate(grid):
            for j, col in enumerate(row):

                if col == "1" and (i, j) not in visited:
                    cnt += 1
                    visited.add((i, j))
                    get_neighbors(i, j)

        return cnt

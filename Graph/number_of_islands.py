class Solution:
    def solve(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[0] * cols for _ in range(rows)]

        def flood_fill(x, y):
            visited[x][y] = 1
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols:
                    if matrix[newx][newy] == 1 and visited[newx][newy] == 0:
                        flood_fill(newx, newy)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and visited[i][j] == 0:
                    island_count += 1
                    flood_fill(i, j)

        return island_count

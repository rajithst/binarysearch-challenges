from collections import deque


class Solution:
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])

        que = deque()
        for i in range(rows):
            for j in range(cols):
                if 0 < j < cols - 1 and 0 < i < rows - 1:
                    continue
                else:
                    if board[i][j] == 1:
                        que.append([i, j])
                        board[i][j] = -1
        while que:
            x, y = que.popleft()
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols and board[newx][newy] == 1:
                    que.append([newx, newy])
                    board[newx][newy] = -1

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0

                if board[i][j] == -1:
                    board[i][j] = 1
        return board
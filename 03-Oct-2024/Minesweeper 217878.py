# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def countMines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            return count

        def dfs(x, y):
            mine_count = countMines(x, y)
            if mine_count > 0:
                board[x][y] = str(mine_count)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
                        dfs(nx, ny)

        click_x, click_y = click
        if board[click_x][click_y] == 'M':
            board[click_x][click_y] = 'X'
        else:
            
            dfs(click_x, click_y)
        
        return board
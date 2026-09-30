class Solution:
    def solve(self, maze, ans, s, vis, row, col, n):
        if row == n - 1 and col == n - 1:
            ans.append(s)
            return

        # downward
        if row + 1 < n and not vis[row + 1][col] and maze[row + 1][col] == 1:
            vis[row + 1][col] = 1
            self.solve(maze, ans, s + 'D', vis, row + 1, col, n)
            vis[row + 1][col] = 0

        if col - 1 >= 0 and not vis[row][col - 1] and maze[row][col - 1] == 1:
            vis[row][col - 1] = 1
            self.solve(maze, ans, s + 'L', vis, row, col - 1, n)
            vis[row][col - 1] = 0

        if col + 1 < n and not vis[row][col + 1] and maze[row][col + 1] == 1:
            vis[row][col + 1] = 1
            self.solve(maze, ans, s + 'R', vis, row, col + 1, n)
            vis[row][col + 1] = 0

        if row - 1 >= 0 and not vis[row - 1][col] and maze[row - 1][col] == 1:
            vis[row - 1][col] = 1
            self.solve(maze, ans, s + 'U', vis, row - 1, col, n)
            vis[row - 1][col] = 0

    def ratInMaze(self, maze):
        n = len(maze)
        ans = []
        s = ""

        if maze[0][0] == 0:
            return ans

        vis = [[0] * n for _ in range(n)]
        vis[0][0] = 1

        row, col = 0, 0
        self.solve(maze, ans, s, vis, row, col, n)

        return ans
    
sol = Solution()

t = int(input())

for _ in range(t):
    n = int(input())
    maze = []
    for i in range(n):
        nums = list(map(int, input().split()))
        maze.append(nums)
    
    ans = sol.ratInMaze(maze)
    print(ans)
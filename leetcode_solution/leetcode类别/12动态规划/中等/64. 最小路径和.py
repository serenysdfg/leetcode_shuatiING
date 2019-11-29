'''给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #me
        m=len(grid)
        n=len(grid[0])
        dp = [[1]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        if m==1 :return sum(grid[0])
        elif n==1:
            for i in range(1,m):
                dp[i][0]=dp[i-1][0]+grid[i][0]
            return dp[m-1][n-1]

        #初始化第一行第一列
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= min(grid[i][j]+dp[i-1][j], grid[i][j]+dp[i][j-1])
        return dp[m-1][n-1]




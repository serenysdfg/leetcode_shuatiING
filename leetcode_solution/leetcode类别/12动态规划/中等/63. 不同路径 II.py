'''有障碍的路径条数'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # copy
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mem = [[0] * n for _ in range(m)]  # 初始化无
        mem[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if j:
                        mem[i][j] += mem[i][j - 1]  # 有障碍0+0
                    if i:
                        mem[i][j] += mem[i - 1][j]
                else:
                    mem[i][j] = 0  # 到障碍物为0

        return mem[m - 1][n - 1]
        # #lose 30min
        # m=len(obstacleGrid)
        # n=len(obstacleGrid[0])
        # if obstacleGrid[m-1][n-1] or obstacleGrid[0][0]:return 0#最后和初始特殊
        # #特殊
        # if m==1:
        #     if sum(obstacleGrid[0])>0:return 0
        #     else:return 1
        # elif n==1:
        #     for i in range(m):
        #         if obstacleGrid[i][0]==1:
        #             return 0
        #     return 1
        # #有1第一行一列不行
        # dp = [[1]*n for _ in range(m)]#主要是一行一列初始化,有阻碍变回0
        # for i in range(n):
        #     if obstacleGrid[0][i]==1:
        #         for j in range(i,n):
        #             dp[0][j]=0
        #         break

        # for i in range(m):
        #     if obstacleGrid[i][0]==1:
        #         for j in range(i,m):
        #             dp[j][0]=0
        #         break

        # print(dp)
        # for i in range(1,m):#还有
        #     for j in range(1,n):
        #         if obstacleGrid[i-1][j]==1 and  obstacleGrid[i][j-1]==1:#有问题？？
        #             return 0
        #         elif obstacleGrid[i-1][j]==1 :
        #             dp[i][j]=dp[i][j-1]
        #         elif obstacleGrid[i][j-1]==1:
        #             dp[i][j]=dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # print (dp)

        # return dp[m-1][n-1]

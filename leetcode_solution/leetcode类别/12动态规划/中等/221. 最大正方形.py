'''在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # 左边右边上边都是同样的数字，加1
        # copy：dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        if not matrix:
            return 0

        res, r, c = 0, len(matrix), len(matrix[0])
        mem = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if not i or not j or matrix[i][j] == '0':
                    mem[i][j] = int(matrix[i][j])
                else:
                    mem[i][j] = min(mem[i - 1][j], mem[i - 1][j - 1], mem[i][j - 1]) + 1
                res = max(res, mem[i][j])
        return res ** 2

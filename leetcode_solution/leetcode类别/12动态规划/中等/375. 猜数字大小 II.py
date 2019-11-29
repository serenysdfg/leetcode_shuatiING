# import functools
class Solution:
    #具体再看
    #但是有一个问题，如果是{1,2,3,4,5},那么二分的思路肯定是先猜3，那么看是大是小，如果大了，就猜2，如果小了，猜4
    #应该先猜4
    def getMoneyAmount(self, n: int) -> int:
#copy1 ok 具体再看
    #需要建立一个二维的dp数组，其中dp[i][j]表示从数字i到j之间猜中任意一个数字最少需要花费的钱数。需要遍历每一段区间[j, i]，维护一个全局最小值global_min变量，然后遍历该区间中的每一个数字，计算局部最大值local_max = k + max(dp[j][k - 1], dp[k + 1][i])，然后更新全局最小值
        # pay = [[0] * n for _ in range(n+1)]
        # for i in reversed(range(n)):#5,4,3,2,1
        #     for j in range(i+1, n): #(3,5)
        #         pay[i][j] = min(k+1 + max(pay[i][k-1], pay[k+1][j])  for k in range(i, j+1))
        # return pay[0][n-1]

        #copy2
        import math
        dp=[[0 for i in range(n)] for j in range(n)]
        I=n-1
        k=1
        while k!=n:
            for i in range(I):
                x=i
                y=i+k
                res=math.inf
                for j in range(x,y+1):
                    if j==x:
                        resi=j+1+dp[j+1][y]
                    elif j==y:
                        resi=dp[x][j-1]+j+1
                    else:
                        resi=j+1+max(dp[x][j-1],dp[j+1][y])
                    if resi<res:
                        res=resi
                dp[x][y]=res
            I-=1
            k+=1
        return dp[0][-1]
    #分治法,超时,但是这个切分点（代码里是 x）不好找，试了几种都不行，干脆枚举了，从 l + r // 2 开始一直到 r - 1

    #     return self.solve(1, n)
    # def solve(self, l, r):
    #     if l == r: return 0
    #     if r - l == 1: return l
    #     if r - l == 2: return l + 1
    #     ans = sum(range(r))
    #     for x in range(l+r>>1, r):
    #         ans = min(max(self.solve(l, x-1), self.solve(x+1, r))+x, ans)
    #     return ans
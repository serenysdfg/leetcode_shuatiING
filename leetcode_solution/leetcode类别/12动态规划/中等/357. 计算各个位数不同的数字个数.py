class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #me
        # 一位一位:组合等2:10+9*9  3:10+9*9+9*9*8；
        #dp[i]+=dp[i-1]+9**
        if n==0:return 1
        elif n==1:return 10
        dp = [0 for i in range(n+1)]
        dp[:1]=[1,10]
        dp[0]=1
        dp[1]=10
        for i in range(2,n+1):
            temp=9
            for j in range(i-1):
                temp*=(9-j)
            dp[i]=dp[i-1]+temp
        return dp[n]
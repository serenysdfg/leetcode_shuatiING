class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划,用字典
        # me超时
        # a={}
        # a[1]=1
        # a[2]=2
        # if n>=3:
        #     a[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        # return a[n]

        # copy
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 2
        b = 3
        for i in range(3, n):  # n=3不会进入循环
            a, b = b, a + b  # 记录前面两个值
        return b

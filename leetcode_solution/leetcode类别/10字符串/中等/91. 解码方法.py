class Solution:
    def numDecodings(self, s: str) -> int:

        # 1copy递归
        # #2 2 1 随机凑,循环,很多种可能，2+1*n 2+2+1*n
        #         如果s[0]和s[0:2]都合法，那么f(s[:])=f(s[1:])+f(s[2:])
        # 如果s[0]合法而s[0:2]不合法的话，那么f(s[:])=f(s[1:])
        # 如s[0]都不合法，那么不可能存在编码

        # 超时
        #     if not s:
        #         return 0

        #     return self._numDecodings(s)

        # def _numDecodings(self, nums):
        #     if not nums: #递归的过程中，递归到了s的末尾了，此时应该返回1，2+0是一种情况
        #         return 1

        #     result = 0
        #     if 1 <= int(nums[0]) <= 9:
        #         result += self._numDecodings(nums[1:])#单个后面继续

        #     if len(nums) >= 2 and 10 <= int(nums[0:2]) <= 26:#两个后面继续
        #         result += self._numDecodings(nums[2:])

        #     return result
        # copy2动态规划
        # f(i)=f(i-1)+f(i-2)
        # 1.s[i-1]单独解码，方法数为dp[i-1]
        # 2.s[i-2:i]拼接成双字符解码，若10<=s[i-2:i]<26，双字符合格，解码的方法数位dp[i-2]，否则为0
        # 综合两种情况，得到状态转移矩阵：
        # dp[i] = dp[i-1] + (dp[i-2] if 双字符合格 else 0)

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            if 9 < int(s[i - 2:i]) < 27:
                dp[i] += dp[i - 2]

        return dp[-1]
        # copy3
        # if not s or s.startswith('0'):
        #     return 0

        # if len(s) == 1 and s[0] != '0':
        #     return 1

        # s_len = len(s)
        # mem = [0 for _ in range(s_len + 1)]
        # mem[0] = 1 if s[0] != '0' else 0
        # mem[1] = 1 if s[1] != '0' else 0

        # for i in range(2, s_len + 1):
        #     if 1 <= int(s[i - 1]) <= 9:
        #         mem[i] += mem[i - 1]
        #     if 10 <= int(s[i-2:i]) <= 26:
        #         mem[i] += mem[i - 2]

        # return mem[-1]
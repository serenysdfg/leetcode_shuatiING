#和279一样
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]=dp
        # 此题可用动态规划求解，类似与背包问题，但每个硬币可用多次
        # dp[i] = min(dp[i-vj]+1)， vj 是硬币的面额
        dp = [float('inf') for i in range(amount + 1)]

        dp[0] = 0

        for i in range(amount + 1):
            # 选更小的dp[i - 1]+1, dp[i - 2]+1, dp[i - 5]) +1;;;i要用coin组合所以i>=coin
            for coin in coins:
                if coin <= i and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1

        return dp[-1] if dp[-1] != float('inf') else -1  # 没变就是不能

        # dp=[-1]*(amount+1)
        # dp[0]=0
        # for i in range(1,amount+1):
        #     for j in range(0,len(coins)):
        #         if i>=coins[j] and dp[i-coins[j]]!=-1:
        #             if dp[i]==-1 or dp[i]>dp[i-coins[j]]+1:
        #                 dp[i]=dp[i-coins[j]]+1
        # return dp[amount]
        # 理解
# 用dp[i] 表示组成 i 元所需要的最小硬币数。
# 对于coins数组里的所有元素j，所有的dp[j] = 1。
# 对于其他的dp[i] = 1 + min(dp[i - 1], dp[i - 2], dp[i - 5])  就是dp[i] = 1 + min(dp[i - j]) for j in coins

# if amount == 0:
#     return 0
# dp = list()
# max_int = 2 << 31

# for i in range(amount + 1):
#     if i not in coins:
#         dp.append(max_int)
#     else:
#         dp.append(1)

# for i in range(amount + 1):
#     if i not in coins:
#         for j in coins:
#             if i - j > 0:
#                 dp[i] = min(dp[i - j] + 1, dp[i])

# return dp[amount] if dp[amount] != max_int else -1

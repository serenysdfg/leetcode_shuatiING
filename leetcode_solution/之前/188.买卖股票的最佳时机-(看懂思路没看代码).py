#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (25.98%)
# Total Accepted:    1.6K
# Total Submissions: 6.1K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# 使用一个global[i][j]来表示前i天最多进行j次交易的最大利润
# 使用一个local[i][j]来表示前i天最多进行j次交易并且第i天进行进行最后一次交易的最大利润
# 接下来需要获得两个变量的推导公式, 首先, global[i][j] 有两种情况:

# 第i天进行第j次交易(局部)
# 第i-1天之前已经进行了j次交易(全局)
# 因此, global[i][j] = max(local[i][j], global[i-1][j]), 注意: 不做特殊说明的话, diff = prices[i] - prices[i-1]

# 接下来, local[i][j]也有两种情况:

# 第i-1天之前进行了j-1次交易(全局), 然后在第i天进行第j次交易, 那么分歧点在于是前一天买入还是当天买入: global[i-1][j-1] + max(diff, 0)
# 把第i-1天进行的第j次交易挪到第i天进行, 也就是: local[i-1][j] + diff
# 从而得到: local[i][j] = max(global[i-1][j-1] + max(diff, 0), local[i-1][j] + diff)

# 这样, 得到遍历公式之后最后取到glocal[len(prices)-1][k]的值即可.

# 最后, 需要特别考虑: 当k远大于len(prices)时, 用动态规划法算法复杂度就很复杂了…

# 这个时候, 问题就退化为了可以进行无限次数交易了, 非常简单: 只要后一天的价格高于当天, 那么就可以买入啦.

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def solveMaxProfit(prices):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] - prices[i-1] > 0:
                    res += prices[i] - prices[i-1]
            return res
        def max(x, y):
            return x if x > y else y
        if k > len(prices):
            # 如果k大于天数, 那么就可以随意交易了
            return solveMaxProfit(prices)
        days = len(prices)
        local_profit = [[0 for _ in range(k+1)] for _ in range(days)]
        global_profit = [[0 for _ in range(k+1)] for _ in range(days)]
        for i in range(1, days):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):
                local_profit[i][j] = max(global_profit[i-1][j-1] + max(diff, 0), local_profit[i-1][j] + diff)
                global_profit[i][j] = max(local_profit[i][j], global_profit[i-1][j])
        #print(global_profit)
        return global_profit[days-1][k]

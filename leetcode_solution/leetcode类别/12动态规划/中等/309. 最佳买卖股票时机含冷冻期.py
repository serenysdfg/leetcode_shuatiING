class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''这是股票系列问题中提到了三种状态buy、sell和cooldown，那么我们脑中的第一个想法就是通过动态规划来解

如果我们index:i天为冷冻期，那么只能说明index:i-1天卖掉了股票，那么i天的收益和i-1天是一样的cooldown[i]=sell[i-1]
如果我们考虑index:i天卖出，要求利润最大的话。一种情况是index:i-1当天买入了股票，另一种情况是index:i-1之前就持有股票，index:i-1天也可以卖出，那么我们就需要考虑index:i-1卖出更好呢？还是index:i卖出更好呢？sell[i]=max(sell[i-1], buy[i-1]+prices[i])

如果我们考虑index:i天买入，要求利润最大的话。一种情况是index:i-1天是冷冻期，另一种情况是index:i-1天不是冷冻期，也就是index:i-1天也可以买入，那么我们就需要考虑index:i-1买入更好呢？还是index:i买入更好呢？buy[i]=max(buy[i-1], cooldown[i-1]-prices[i])
我们第一天不可能卖出或者冻结，那么这两个sell[0]=0 cooldown[0]=0，但是我们第一天可以买入啊，所以buy[0]=-prices[0]。还有一点要注意的就是，我们一定是最后一天卖出或者最后一天冻结利润最大。
'''
        #copy
        if not prices:
            return 0
        #多种状态
        len_prices = len(prices)
        buy, sell, cooldown = [0]*len_prices, [0]*len_prices, [0]*len_prices
        buy[0] = -prices[0]#利润
        for i in range(1, len_prices):
            cooldown[i] = sell[i-1]
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])#前一次sell或者买入卖出
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])

        return max(sell[len_prices - 1], cooldown[len_prices - 1])  
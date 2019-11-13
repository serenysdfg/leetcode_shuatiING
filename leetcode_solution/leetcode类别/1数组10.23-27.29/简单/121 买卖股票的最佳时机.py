class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #买入的数组copy  :最大结尾-最小初始
        if not prices or len(prices) == 0:
            return 0
        res, max_cur = 0, 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur+prices[i]-prices[i-1]) #后面数-最小,正就可以,变负数就有更小的初始: 如果正,,继续加后面两个差值:如果今天卖相比于昨天卖能多赚，则今天卖，否则之前就卖了
            res = max(res, max_cur)#曾经最大+现在新的大值比较
        return res
        
        #solution2
        # if len(prices) < 2:
        #     return 0
        # min_price = prices[0]
        # max_profit = 0
        # for price in prices:
        #     if price < min_price: #获取最小
        #         min_price = price
        #     if price - min_price > max_profit:
        #         max_profit = price - min_price
        # return max_profit

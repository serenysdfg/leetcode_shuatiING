'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


定义dp[i][j]为word1中前i个字符组成的串，与word2中前j个字符组成的串的编辑距离。
插入操作：在word1的前i个字符后插入一个字符，word2[j+1]。i是没有前进的。所以此时是dp[i][j]=dp[i][j-1]+1
删除：删除在word1的第i个字符dp[i][j]=dp[i-1][j]+1
替换:dp[i][j]= dp[i-1][j-1]+(word1[i-1] !=word2[j-1])#前面不同+1，前面相同+0  ？？ #边界


'''
from heapq import heappush, heappop


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # copy3
        word1_len, word2_len = len(word1), len(word2)
        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]  # dp多一个因为从1开始
        for i in range(1, word1_len + 1):  # 前i个字符和前0个，要不断删除
            dp[i][0] = i
        for j in range(1, word2_len + 1):  # 要不断增加
            dp[0][j] = j

        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]), dp[i][j - 1] + 1, dp[i - 1][j] + 1)#前面不同+1，前面相同+0，没看懂

        return dp[-1][-1]

        # copy2

        # m=len(word1)+1
        # n=len(word2)+1
        # dp = [[0 for i in range(n)] for j in range(m)]

        # for i in range(n):
        #     dp[0][i]=i
        # for i in range(m):
        #     dp[i][0]=i
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        # return dp[m-1][n-1]

        # #copy1没看
        '''空间复杂度优化为O(n)级别，但其实数组开辟空间和赋值操作也就同样的增加了时间损耗。

由于问题是求最少操作数，所以我们很容易想到通过广度优先遍历来解。只是这里的广度优先遍历和以往的有些区别，我们每次需要访问的边有四种。也就是前文说的word1[i-1]==word2[j-1]的一种情况和word1[i-1]!=word2[j-1]的三种情况。实际的操作过程非常容易，代码如下
'''
        # heap = [(0, word1, word2)]
        # visited = set()
        # while heap:
        #     d, w1, w2 = heappop(heap)
        #     if (w1, w2) in visited:
        #         continue
        #     visited.add((w1, w2))    
        #     if w1 == w2:
        #         return d #次数
        #     if w1 and w2 and w1[0] == w2[0]:
        #         heappush(heap, (d, w1[1:], w2[1:]))
        #     else:
        #         if w1: 
        #             heappush(heap, (d+1, w1[1:], w2)) #delete
        #         if w1 and w2: 
        #             heappush(heap, (d+1, w1[1:], w2[1:])) #replace
        #         if w2: 
        #             heappush(heap, (d+1, w1, w2[1:])) #add


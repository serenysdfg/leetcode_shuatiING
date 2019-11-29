class Solution:
    def countBits(self, num: int) -> List[int]:
        ##copy1:如果一个数 i 和 i - 1 做与运算，那么 i 的二进制表示形式中的最右边一个 1 会变成0 。根据这个结论可以优化统计每个数中 1 的个数的函数getOne。
        res = list()
        for i in range(num + 1):
            res.append(self.getOne(i))

        return res

    def getOne(self, n):
        cnt = 0
        while (n):
            cnt += 1
            n = n & (n - 1)
        return cnt
        # copy2   i & i -1 这个数字的1的个数cnt，那么根据上面的提到的结论， i 这个数字中 1 的个数就是 cnt + 1。(重要)
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp
        # copy3  不好:每个数都按照常规方法（不断除以2）求其二进制中有多少个1。
        res = list()
        for i in range(num + 1):
            res.append(self.getOne(i))

        return res

        def getOne(self, n):
            binary = list()
            while (n >= 2):
                binary.append(n % 2)
                n = n // 2
            binary.append(n)
            # print binary
            return sum(binary)

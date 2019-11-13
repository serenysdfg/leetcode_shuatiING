class Solution:
    def getSum(self, a: int, b: int) -> int:
        #copy
        # 解析：https://blog.csdn.net/qq_34364995/article/details/80738911
        #     https://blog.csdn.net/liyuanbhu/article/details/51803974
        mask = 0xffffffff # 是一个负数的补码。
        while b & mask: #b!=0
            a, b = a ^ b, (a & b) << 1

        return a & mask if b > mask else a
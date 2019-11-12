'''计算并返回
x
的平方根，其中
x
是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # 还有牛顿法？
        # copy二分查找，不太懂
        res = x
        while res ** 2 > x:
            res = (res + x // res) // 2

        return res
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = list()
        add, l1, l2 = 0, len(a), len(b)
        while add or l1 or l2:
            if l1:
                l1 -= 1
                add += int(a[l1])
            if l2:
                l2 -= 1
                add += int(b[l2])
            res.append(str(add & 1))  # 存储最后一个数到前面的数
            add >>= 1  # 用于进位

        return ''.join(reversed(res))
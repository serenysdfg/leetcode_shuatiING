class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = L = 0         
        for i in s:
            if i == 'L': #只计算L个数+-1
                L += 1
            else:
                L -= 1
            if L == 0:
                res += 1
        return res
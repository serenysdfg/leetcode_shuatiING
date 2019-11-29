class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num=bin(n)
        for i in range(3,len(num)):
            if num[i-1]==num[i]:
                return False
        return True
#简单
#me
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            n = num
            num = 0
            while n > 0:
                num += n % 10
                n = n // 10
        return num


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        count=0
        a=num
        while num > 1:
            num >>= 2
            count+=1
        if a/pow(4,count)==1:
            return True
        else:
            return False
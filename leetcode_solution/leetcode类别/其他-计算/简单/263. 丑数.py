class Solution:
    def isUgly(self, num: int) -> bool:
        #只能被质数整除。质数不断相加，还有一题难一点的？忘了哪题
        #me
        if num == 0 : return False  #重要，不然超时 0%2始终是0
        while num%2==0:
            num//=2
        while num%3==0: #能被整除
            num//=3
        while num%5==0:
            num//=5
        if num==1:return True
        return False
        #copy
        for p in [2, 3, 5]:
            while num and num%p == 0:
                num //= p
        return num == 1

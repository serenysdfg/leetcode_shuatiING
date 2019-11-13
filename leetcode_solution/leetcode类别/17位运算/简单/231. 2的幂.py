class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # copy位运算

        # positive x is a power of two ⇔ (x & (x − 1)) is equal to zero.
        # return n & (n-1) == 0 if n != 0 else False #特殊
        # #copy2递归重复操作
        # if n <= 0:
        #     return False
        # if n == 1:
        #     return True
        # if n % 2 == 0:
        #     return self.isPowerOfTwo(n/2)
        # return False

        # #copy1
        # for i in range(64):
        #     j = 2**i
        #     if j == n:
        #         return True
        #     if j >n:
        #         return False
        # #me
        # if n==0 :return False #注意
        # if n==1:return True
        # while n>1:
        #     temp=n
        #     n//=2
        #     m=temp%2
        #     if m!=0: #注意
        #         return False
        #     if n==1:
        #         if temp%2==0:
        #             return True
        #         else:
        #             return False
        # me改进
        while n > 0:
            if n % 2 == 0:
                n = n / 2
            else:
                break
        return n == 1



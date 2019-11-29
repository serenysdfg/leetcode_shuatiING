# class Solution:
# 因为n最大是32，所以我们可以先把所有的数给算出来，然后只要对输入的数在字典中查询即可。
# d = dict()
# def tribonacci(self, n: int) -> int:
#     def tri(x):
#         n, a, b, c = 0, 0, 1, 1
#         while n < x:
#             yield a + b + c
#             a, b, c = b, c, a + b + c
#             n += 1

#     if n in self.d:
#         return self.d[n]

#     for i, v in enumerate(tri(35)):
#         self.d[i + 3] = v
#     self.d[0], self.d[1], self.d[2] = 0, 1, 1
#     return self.d[n]
# 2
class Solution:
    d = dict()

    def tribonacci(self, n: int) -> int:
        t = [0] * 38
        t[0], t[1], t[2] = 0, 1, 1
        for i in range(3, n + 1):
            t[i] = t[i - 1] + t[i - 2] + t[i - 3]
        return t[n]

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        else:
            res = self.tribonacci[n - 1] + self.tribonacci[n - 2] + self.tribonacci[n - 3]
        return res
        # me超时
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n==0:return 0
#         elif n==1:return 1
#         elif n==2:return 1

#         else:
#             # res=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)#每个一都要操作很长时间，超时，错误
#         return  res

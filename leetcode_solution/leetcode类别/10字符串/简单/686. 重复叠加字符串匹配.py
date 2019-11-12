'''给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。

答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

注意:

 A 与 B 字符串的长度在1和10000区间范围内。'''
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not set(B).issubset(set(A)):
            return -1
        num = 1
        S = A
        while len(S) < len(B):
            S += A
            num += 1
        if B in S:
            return num
        if B in S+A:
            return num+1
        return -1
        #思路要清晰，列出各种可能
# 如果B中字符有不在A中的，返回-1
# 如果A的长度 < B的长度，那么B不可能是A的子串，需要先将A重复到长度 >= B
# 如果A的长度 >= B的长度，
# 2.1. 如果此时A包含B,，么返回之前A重复的次数
# 2.2. 如果此时A不包含B，那么将A再重复一次
# 2.2.1 如果此时A包含B，那么返回之前A重复的次数
# 2.2.2 如果此时A不包含B，那么返回-1--字符串A复制一遍不包含字符B，那么无论复制多少遍也不包含字符B，控制长度在len(A)2即可#




#2
    # 如果字符串A比字符串B长：
# （1）字符串A本来就包含字符串B，这时A仅复制一遍就找到了，最大长度为len(A)；
# （2）字符串A复制一遍包含字符B，这时A的重复次数为2，遍历控制范围是len(A)2；
# （3）字符串A复制一遍不包含字符B，那么无论复制多少遍也不包含字符B，控制长度在len(A)2即可。

# 如果字符串A比字符串B短，我们将字符串A复制到刚好大于字符串B的长度，长度控制为不小于len(B)时跳出循环。

# 以上两种情况取最大值，求和即可：len(A)*2+len(B)。

# class Solution:
#     def repeatedStringMatch(self, A: str, B: str) -> int:

#         A_repeat, r = A, 1
#         while len(A_repeat) < 2 * len(A) + len(B):
#             if B in A_repeat:
#                 return r
#             A_repeat, r = A_repeat + A, r + 1

#         return -1
        #失败
        # count=0
        # for i in B:
        #     if i not in A:
        #         return -1
        # if len(A)<len(B):
        #     if len(B)%len(A)==0:
        #         a=len(B)//len(A)*A
        #         count=len(B)//len(A)
        #     else:
        #         a=(len(B)//len(A)+1)*A
        #         count=len(B)//len(A)+1
        # if B in a:
        #     return count
        # else:
        #     a=a*2
        #     print(a)
        #     if B not in a:
        #         return -1
        #     else:
        #         return count*2


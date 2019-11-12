class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # ok：k相加，前面的反转,i+k超出也可以

        a = []
        i = 0
        while i < len(s):
            a.append(s[i:i + k][::-1])
            a.append(s[i + k:i + 2 * k])
            i += 2 * k

        return ''.join(i for i in a)

    # copy
#         j = 1
#         str2 = ''
#         for i in range(0,len(s),k):
#             if j == 1:
#                 str2 += s[i:i+k][::-1] #轮流j=1，2，i+k超出也可以
#                 j = 2
#             elif j==2:
#                 str2 += s[i:i+k]
#                 j = 1
#         return str2



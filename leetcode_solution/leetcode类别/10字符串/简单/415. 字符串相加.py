'''给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
# t投机取巧
# def str2int(num):
#     res = 0
#     for i in range(len(num)-1, -1, -1):
#         res += int(num[i]) * pow(10, len(num)-1-i) #每一位都是，一位一位转整数
#     return res
# return str(str2int(num1) + str2int(num2))
# 前面补充0
# copy对
        i = len(num1) - 1
        j = len(num2) - 1
        result = ''
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0') #重要转化成ord
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            result += chr(carry % 10 + ord('0')) #ord(num1[i]) - ord('0')
            carry //= 10
            i -= 1
            j -= 1
        if carry == 1:
            result += '1'
        return result[::-1]

# 错误
#         p=len(num1)
#         q=len(num2)
#         if p>=q:
#             num2=(p-q)*'0'+num2
#         else:
#             num1=(q-p)*'0'+num1
#         #个位数相加
#         a=[]
#         b=0
#         print(num1)
#         if len(num1)==1:
#             return str(int(num1[0])+int(num2[0]))
#         for i in range(len(num1)-1,-1,-1):
#             print(i)
#             print("565")
#             a.append((int(num1[i])+int(num2[i]))%10+b)
#             b=(int(num1[i])+int(num2[i])+b)//10
#             print(a)
#             print(b)
#         if b==1:
#             a.append(b)
#         return ''.join(str(i) for i in  a[::-1])




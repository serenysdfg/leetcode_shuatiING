#  从前向后依次扫描，用一个临时变量记录当前数字。
# 如果没有出现题目中出现的特殊情况，那我们就可以一直一个一个加下去，这样就能得到正确结果。（先思考：）
# 特殊情况出现的时候，后一位数字比前一位数字大，而正常情况正好是相反的（后一位数字一定比前一位小），后一位减去前一位即可得到这两位得到的数值，但是要注意一点，我们在这之前已经将前一位进行加和了一次，所以这时候，我们要减去 2 次前一位数字。
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        res = 0
        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i-1]]:#后面的更大
                res = res + lookup[s[i]] - 2 * lookup[s[i-1]]
            else:
                res += lookup[s[i]]
        return res
  #没看
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         #copy
#         # 创建字典
#         dict = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#             'IV': 4,
#             'IX': 9,
#             'XL': 40,
#             'XC': 90,
#             'CD': 400,
#             'CM': 900
#         }

#         sum = 0
#         str = ''
#         for i in range(len(s)):
#             str = str + s[i]
#             if i != len(s)-1:
#                 if dict[s[i]] < dict[s[i + 1]]:
#                     continue
#                 else:
#                     sum = sum + dict[str]
#                     str = ''
#             else:
#                 sum = sum + dict[str]
#                 str = ''

#         return sum

'''罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def intToRoman(self, num: int) -> str:
        # copy
        lookup = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        romanStr = ''

        for symbol, val in sorted(lookup.items(), key = lambda t: t[1], reverse = True):
        	while num >= val:
        		romanStr += symbol#减去最大的
        		num -= val
        return romanStr
        # copy2
        # M = ['', 'M', 'MM', 'MMM']  # 0,1000,2000,3000
        # C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']  # 0,100,200,300,...,900
        # X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']  # 0,10,20,30,...,90
        # I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']  # 0,1,2,3,...,9
        #
        # result = M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
        # return result
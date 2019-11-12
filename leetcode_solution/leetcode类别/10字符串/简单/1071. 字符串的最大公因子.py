class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str2==str2:return str1
        # 辗转相除法   #Copy
        #         例如:找到25和10的最大公约数
        # 25 / 10 = 2 余数 5
        # 10 / 5 = 2 余 0
        # 5就是最大公约数，此题同理
        # l1, l2 = len(str1), len(str2)
        # if l2 > l1:#使得l1比较长
        #     str1, str2 = str2, str1
        #     l1, l2 = l2, l1
        # if l1 == l2:
        #     return str1 if str1==str2 else ''
        # f = l1%l2
        # if f == 0:
        #     return str2 if str2*(l1//l2)==str1 else ''
        # else:
        #     return self.gcdOfStrings(str2, str1[-f:])#
#copy没仔细看
        sort_str = lambda s1, s2: (s2, s1) if len(s2) > len(s1) else (s1, s2)
        long, short = sort_str(str1, str2)
        while long != short:
            if short not in long:
                return ''
            long = long.replace(short, '', 1)
            long, short = sort_str(short, long)
        return short
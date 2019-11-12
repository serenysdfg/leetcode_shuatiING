'''给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # res, m, n = 0, len(num1), len(num2)

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         res += int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2)#每一位
        # return str(res)
        #         m位的数字乘以n位的数字的结果最大为m+n位：只用字符串不用加减
        # 99999 < 1000100 = 100000，最多为3+2 = 5位数。
        # 先将字符串逆序便于从最低位开始计算。
        lookup = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9}  # 节省查找时间，避免无休止使用ord函数来得到数字
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]

        tmp_res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i + j] += lookup[num1[i]] * lookup[num2[j]]  # 重点i+j）*100

        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1) + len(num2)):
            res[i] = tmp_res[i] % 10  # res保留当前位
            if i < len(num1) + len(num2) - 1:
                tmp_res[i + 1] += tmp_res[i] / 10  # 上升一位
        return ''.join(str(i) for i in res[::-1]).lstrip('0')  # 去掉最终结果头部可能存在的‘0’，反过来
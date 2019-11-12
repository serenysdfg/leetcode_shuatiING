class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:#bin(h) 转化成二进制：回溯，满足就继续添加，不满足下一个循环
                    ans.append('%d:%02d' % (h, m))

        return ans
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 简单11min
        # 计数能组成几个
        a = []
        for s in 'ban':
            a.append(text.count(s))
        a.append(text.count('l') // 2)
        a.append(text.count('o') // 2)

        return min(a)

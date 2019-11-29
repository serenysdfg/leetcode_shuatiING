class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 可以换顺序,,题意读清
        d = {}
        count = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
        for key, value in d.items():
            if value % 2 == 1:
                count += 1  # 奇数个数
        if count:
            length = len(s) - count + 1
        else:
            length = len(s)
        return length


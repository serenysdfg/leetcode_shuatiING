# from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        # dict=Counter(s)
        # if dict['A']>1:return False

        if s.count("A") > 1: return False
        for i in range(len(s) - 2):
            if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
                return False
        return True


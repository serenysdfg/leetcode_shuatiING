#简单
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # j
        count=0
        for s in S:
            if s in J:
                count+=1
        return count
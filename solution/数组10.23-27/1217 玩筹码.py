class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        #copy
        res = [0, 0]
        for c in chips:
            res[c % 2] += 1 #余数移动一个单位，偶数位，奇数位
        return min(res)
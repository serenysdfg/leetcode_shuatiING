class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        #copy#未看
        
        res = []
        for i in range(R):
            for j in range(C):
                res.append(([i, j], abs(r0 - i) + abs(c0 - j)))
        res = sorted(res, key=lambda res: res[1])
        res = [v[0] for v in res]
        return res
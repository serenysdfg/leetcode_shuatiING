class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #copy
        # res = [[1]]
        # for i in range(1, numRows):
        #     res.append(map(lambda x,y:x+y, [0]+res[-1], res[-1]+[0]))
        # return res[:numRows]
    
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[-1][j-1]+res[-1][j])
            tmp.append(1)
            res.append(tmp)
        return res      
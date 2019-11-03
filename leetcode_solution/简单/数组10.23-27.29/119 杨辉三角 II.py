class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(1, rowIndex+1):#5行,生成4条就可以
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[j-1]+res[j]) #append,最后一行res[-1]0+1  1+2  2+...+j
            tmp.append(1)
            res=tmp#数组存储,先算tmp
        return res
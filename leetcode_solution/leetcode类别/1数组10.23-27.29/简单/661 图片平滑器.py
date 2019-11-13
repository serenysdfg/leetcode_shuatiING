'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
注意:
官方授权，非商业转载请注明出处。
'''
class Solution:
    def isLegal(self,x,y,i,j):
        return (True if((i<x)and(j<y)and(i>=0)and(j>=0)) else False)#是否存在

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        #copy2

        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x=len(M)
        y=len(M[0])
        returnM=copy.deepcopy(M)
        # returnM=M
        Filter=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]#八个位置
        for i in range(x):
            for j in range(y):
                legalPointNum=0 #计数
                graySum=0 #总和
                for fi in range(9):#8个
                        tmpi=i+Filter[fi][0]
                        tmpj=j+Filter[fi][1]
                        if(self.isLegal(x,y,tmpi,tmpj)):
                            # print(tmpi)
                            # print(tmpj)
                            graySum+=M[tmpi][tmpj] #存在加上去
                            legalPointNum+=1
                # print(graySum)
                # print(legalPointNum)
                returnM[i][j]=int(graySum/legalPointNum)
        return returnM

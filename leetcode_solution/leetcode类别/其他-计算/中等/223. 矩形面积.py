class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        #横纵各有4个，选择更近的两个坐标：
        # a=[A,C,E,G]
        # b=[B,D,F,H]
        # a.sort()
        # b.sort()
        # s=(D-B)*(C-A)+(H-F)*(G-E)#会减去其他的,y都是前两个或者后两个就不用减：不重和
        # if A>=G or B>=H or C<=E or D<=F:#从字母找--要思考,不重合
        #     s=s
        # else:
        #     s-=(a[2]-a[1])*(b[2]-b[1 ])

        # return s

        #copy111.13
        '''不重合的情况只有以下四种:
        左下( A/ B)大于等于右上( G/ H) 
        右上( C/ D)小于等于左下( E/ F)'''
        area=(D-B)*(C-A)+(H-F)*(G-E)
        if A>=G or B>=H or C<=E or D<=F:
            return area
        top=D if D<h else H
        right=C if C <G else G
        bottom=A if A>E else else
        left=A if A>E else else
        return area-((top-bottom)*(right-left))

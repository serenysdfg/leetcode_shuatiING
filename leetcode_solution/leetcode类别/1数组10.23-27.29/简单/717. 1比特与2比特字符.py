class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #找规律题
        #倒数第三位如果是0肯定为False,如果是1待定，继续往下分析  copy
        bits_reverse = bits[::-1]
        bits_reverse.append(0)
        id1 = [i for i,x in enumerate(bits_reverse) if x==0] #只获取0
        if id1[1] % 2 == 0:
            return False
        else:
            return True



#lose不谨慎
        # if len(bits)==1:return True
        # elif bits[-2:]==[0,0]:return True
        # elif len(bits)<4 and  bits[-3:]==[1,1,0]:
        #     return True
        # elif len(bits)>=4 and bits[-4:]==[0,1,1,0]:
        #     return True
        # return False

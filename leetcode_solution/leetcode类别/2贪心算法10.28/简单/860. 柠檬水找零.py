class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #要计数5，10有多少
        count=[0,0,0]
        # if (len(bills)==0 or bills[0]>5):return False
        for  i in range(0,len(bills)):
            if bills[i]==5:
                count[0]+=1
            elif bills[i]==10:
                count[0]-=1
                count[1]+=1
            elif bills[i]==20:
                if count[1]==0:#出错，还可以三张5元，没有10的话
                    count[0]-=3
                else:
                    count[0]-=1
                    count[1]-=1
                    count[2]+=1

            if (count[0]<0 or count[1]<0):
                return False
        return True
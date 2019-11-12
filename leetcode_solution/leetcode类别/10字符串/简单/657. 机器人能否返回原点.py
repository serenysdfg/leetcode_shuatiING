class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=[0,0]
        for i in moves:
            if i=="U":
                a[0]+=1
            elif i=="D":
                a[0]-=1
            elif i=="L":
                a[1]+=1
            elif i=="R":
                a[1]-=1
        if a[0]==0 and a[1]==0:
            return True
        else:
            return False 
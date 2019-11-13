class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #先排序
        g.sort()
        s.sort()
        i,j,count=0,0,0
        while(i<len(s) and j <len(g)):

            if s[i]>=g[j]:
                i+=1
                j+=1
                count+=1
            else:
                i+=1
        return count
                    
        
        
        

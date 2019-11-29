class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #写法较复杂--弄清楚自己些copy
        #动态规划换个花样:突然要返回一个解
        #排序后，dp[i]是第i个数字结尾的数组段所能拥有的最大整数子集长度。
        #很显然，dp[i]=max（dp[a1],dp[a2]...dp[ak]）+1，其中dp[ax]代表能实现dp[i]%dp[ax]==0，

        #也就是说dp【i】是所有在i前面的数字能构造最大整除子集的最长的再加1.
        # 用了下标数组来解决解的保存,union-find算法，先把坐标设为-1，如果合并两个集合，就把其中一个index[i]=j这样就有i，j合并,dp中记录下标合并交集
        if len(nums)==1:return nums

        nums.sort()
        dp=[0 for x in range(len(nums))]
        index=[-1 for x in range(len(nums))]
        max_len,max_index=0,-1
        for i in range(len(nums)):
            dp[i]=1
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:#获取最大max循环
                    dp[i]=dp[j]+1
                    index[i]=j#那个j+最后一个数,ij合并  解的保存  i后面的一个,j倒数第二个
                if dp[i]>max_len:
                    max_len=dp[i]#记录最大长度
                    max_index=i #最大长度的最后一个数字位置
        arr=[]
        while True: #max_index==-1结束循环
            if max_index!=-1:
                arr.append(nums[max_index]) #获取
                max_index=index[max_index]
            else:
                break
        return arr[::-1]

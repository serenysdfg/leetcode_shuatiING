class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #方法，一个最大一个负数记录
        #连接  https://blog.csdn.net/qq_17550379/article/details/83659754
        #dp#负数想，# dp[i]=max(dp[i-1]*nums[i],)错
        #可不可以记录+的和-的，记录两个dp数组，我哭了，真的是这样做的
        n = len(nums)
        maxdp = [ nums[0] for i in range(n)]#最大
        mindp = [ nums[0] for i in range(n)]#最小


        for i in range(1,n):
        	maxdp[i] = max(mindp[i-1]*nums[i], maxdp[i-1]*nums[i],nums[i])
        	mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i],nums[i])

        return max(maxdp)
        #当遇到负数的时候，负数乘最大值就变成了最小值，所以应该在比较之前把imax和imin调换

        Max = nums[0]
        imax,imin=1,1
        for i in nums:
            if i < 0:
                imax,imin=imin,imax
            imax= max(imax*i,i)
            imin=min(imin*i,i)
            Max = max(imax,Max)
        return Max

        #copy2
        B = nums[::-1] #倒过来
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)

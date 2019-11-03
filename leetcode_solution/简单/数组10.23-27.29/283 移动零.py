class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #2copy两个idx ，最好
        # cur ,idx=0,0
        # while(idx<len(nums)):
        #     if(nums[idx]!=0):
        #         nums[cur]=nums[idx]
        #         cur+=1
        #     idx+=1
        # while(cur<len(nums)):
        #     nums[cur]=0
        #     cur+=1
        #3copy双指针
        p0, p1 = 0, 0  # P1指向非0，p0指向0
        while p0 < len(nums) and p1 < len(nums):
        	if nums[p0] != 0:
        		p0 += 1
        		p1 = p0
        		continue
        	if nums[p1] == 0:
        		p1 += 1
        		continue
        	nums[p0],nums[p1] = nums[p1],nums[p0]
        	p0 += 1
        	p1 += 1  
        #1copy 暴力
        # i = 0
        # while 0 in nums:
        #     nums.remove(0)
        #     i += 1
        # nums.extend([0]*i)
        #mysol，不能全部通过，没有0的时候失败
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i]!=0:
#                 for j in range(i,len(nums)):
#                     nums[j-i]=nums[j]
#                 for k in range(len(nums)-i,len(nums)):
#                     nums[k]=0
                
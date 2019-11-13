class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #copy
        nums.insert(0, 0)
        x = 0
        #只是删哪个元素，更大的还是更小的，要测试 if 条件 。例如 [1, 5 ,8 , 6] , [2 , 3 ,2 ,6] ,
        # [1, 3 ,5 , 1 ,2 ]#只有x=1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1]:
                if nums[i-1] > nums[i+1] and i+2 < len(nums) and nums[i] > nums[i+2]:#两次递增
                    return False
                x += 1
                if x > 1:
                    return False
        return True
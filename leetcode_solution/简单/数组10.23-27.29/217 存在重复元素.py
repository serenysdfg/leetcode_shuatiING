class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #copy
        return len(nums) != len(set(nums))
        #copy2
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        #超时
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]==nums[j]):
        #             return True
        # return False
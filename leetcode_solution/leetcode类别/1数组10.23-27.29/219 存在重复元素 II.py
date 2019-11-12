class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # for i in range(len(nums)-1):
        #     for j in range(1,len(nums)-i):
        #         if nums[i] == nums[i+j]:
        #             return True
        # return False
    # copy
    # 这个元素还没出现过，就以 <num, index> 的形式存进字典里，如果 num 再次出现了，计算相邻距离，小于等于 k 则 return true
        lookup = {}
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            else:
                if i - lookup[nums[i]] <= k:
                    return True
                else:
                    lookup[nums[i]] = i
        return False
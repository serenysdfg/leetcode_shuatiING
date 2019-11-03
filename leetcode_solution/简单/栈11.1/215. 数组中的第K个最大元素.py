from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #1堆
        # heapify(nums)
        # while len(nums)>k:
        #     heappop(nums)
        # return nums[0]
     #2数组
        nums.sort(reverse=True)
        return nums[k-1]
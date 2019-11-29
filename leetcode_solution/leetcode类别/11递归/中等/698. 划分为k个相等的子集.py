class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #递归copy

        sum_nums = sum(nums)
        avg = sum_nums // k
        if k <= 0 or sum_nums % k != 0 or max(nums) > avg:#要整数，最大的不能大于平均，不然一个就不满足
            return False
        n= len(nums)
        visited = [0] * n #是否访问过
        nums = sorted(nums, reverse=True)#牌组
        return self.canPartition(nums, visited, 0, k, 0, 0, avg)
    def canPartition(self, nums, visited, start_index, k, cur_sum, cur_num, target):
        if k == 1:#分成一组
            return True
        if cur_sum == target and cur_num > 0:#cur_num > 0加上了一个值，=0就没有加上
            return self.canPartition(nums, visited, 0, k - 1, 0, 0, target)#取出一个了，分成k-1组
        if cur_sum > target:
            return False
        for i in range(start_index, len(nums)):
            if visited[i] == 0:
                visited[i] = 1
                if self.canPartition(nums, visited, i + 1, k, cur_sum + nums[i], cur_num + 1, target):#start_index变成i+1该值visited=1，sum加上去
                    return True
                visited[i] = 0
        return False

class NumArray:

    def __init__(self, nums: List[int]):
        # copy
        self.sums = nums
        for i in range(1, len(self.sums)):
            self.sums[i] = self.sums[i - 1] + self.sums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
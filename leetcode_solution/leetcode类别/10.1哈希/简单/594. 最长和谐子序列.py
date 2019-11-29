class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count, res = Counter(nums), 0                           # 统计列表中各个元素出现次数，并初始化结果为零
        for num, count in num_count.items():                        # 考察字典中每一条数字-次数对
            if num+1 in num_count.keys():                           # 如果数字+1也在字典中
                res = max(num_count[num]+num_count[num+1], res)     # 组成和谐数组并统计当前最大长度,max使用
        return res


        # if nums:
        #     dic_nums = collections.Counter(nums)
        #     flag = nums[0]
        #     max1 = 0
        #     nums =sorted(nums)
        #     for i in range(1,len(nums)):
        #         if nums[i] - flag == 1:
        #             max1 = max(max1,dic_nums[flag]+dic_nums[nums[i]])
        #         flag = nums[i]
        #     return max1
        # else:
        #     return 0
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter, (nums1, nums2))#对每个数计数
        return list((a & b).elements())
#         #双指针
#         nums1.sort()
#         nums2.sort()
#         l1 = len(nums1)
#         l2 = len(nums2)
        
#         p1 = 0
#         p2 = 0
        
#         res = []
        
#         while p1 < l1 and p2 < l2:#排序后和另一个数组的每一个相比
#             if nums1[p1] < nums2[p2]:
#                 p1 += 1
#             elif nums1[p1] > nums2[p2]:
#                 p2 += 1
#             else:
#                 res.append(nums1[p1])
#                 p1 += 1
#                 p2 += 1
#         return res
#未看
        record, result = {}, []
        for num in nums1:
            record[num] = record.get(num, 0) + 1
                
        for num in nums2:
            if num in record and record[num]:
                result.append(num)
                record[num] -= 1
        return result

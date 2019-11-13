class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #copy
        # 因为时间复杂度为O(N), 所以只能一一最好
        r = [float("-inf"), float("-inf"), float("-inf")]
        for n in nums:
            if n>r[0]:
                r=[n,r[0],r[1]]
            elif n>r[1] and n <r[0]:
                r = [r[0], n, r[1]]
            elif n > r[2] and n< r[1]:
                r[2] = n
        return r[0] if math.isinf(r[2]) else r[2]
        


#         m, sm, tm = float('-inf'), float('-inf'), float('-inf')

#         for num in nums:
#             if num > m:
#                 tm = sm
#                 sm = m 
#                 m = num
#             elif num < m and num > sm:
#                 tm = sm
#                 sm = num
#             elif num < m and num < sm and num > tm:
#                 tm = num

        return tm if tm != float('-inf') else m 
        #myso块
#         nums=list(set(nums))
#         nums.sort(reverse=True)
#         if len(nums)<3:
#             return nums[0]
#         else:
#             return nums[2]
        
        
        
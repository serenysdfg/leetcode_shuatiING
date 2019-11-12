class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # #递归copy,最后一位>9，添加一个0，然后再把余下的递归加1,用递归,因为每一位都是相同处理
        # if digits == []:
        #     return [1]
        # if digits[-1] < 9:
        #     return digits[:-1] + [digits[-1] + 1]
        # else:
        #     return self.plusOne(digits[:-1]) + [0] #剩下的递归,后面补0
        #copy循环，效率更高.后一位有进位的话，那么该位要加上一
        carry = 1#标志最前面不用+1

        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] < 10:#结束
                carry = 0
                break
            else: #继续加i向前
                digits[i] -= 10
        if carry == 1:
            digits.insert(0,1)
        return digits
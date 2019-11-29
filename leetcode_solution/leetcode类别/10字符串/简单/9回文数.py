# 重要：首先负数肯定不是palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(str(x))):
            left, right = 0, len(x) - 1
            while left < right:
                if x[left] != x[right]:
                    return False
                left += 1
                right -= 1
        return True
        # 通过字符串进行反转，对比数字是否相等就行
        # 首先负数肯定不是palindrome
        if x < 0:
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return True
            # copy2
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x /= 10
        return y == rev

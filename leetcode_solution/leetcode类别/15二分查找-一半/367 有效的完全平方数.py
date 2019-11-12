class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 4 : return True
        for i in range(num//2):
            if i*i == num:
                return True
            elif i*i > num:
                return False
        return False
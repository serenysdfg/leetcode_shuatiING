class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x^y).count('1') #字符串的count
        # me
        # a=bin(x^y)
        # count=0
        # for i in a:
        #     if i=='1':
        #         count+=1
        # return count
        a = x ^ y
        count = 0
        while a != 0:
            if a % 2 == 1:  # 计算个数
                count += 1
            a >>= 1  # 除以2
            # count+=1
        print(count)
        return count

''.join([str(1 - int(i)) for i in list(num[pos:])])
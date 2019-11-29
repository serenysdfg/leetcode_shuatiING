class Solution:
    def findComplement(self, num: int) -> int:
        # me 用到 int('011',2)  ''.join(['a','b'])   str(i) for i in list(a)
        return int(''.join([str(1 - int(i)) for i in list(bin(num)[2:])]), 2)  # 前面都是0b  pos直接为2

        # copy
        i = 1 << (len(bin(num)) - 2)  # 因为bin函数转化成的格式是‘0bXXXX’，头两个‘0b’要减掉去
        return (i - 1) ^ num  # return (i - 1) - num # 这样也可以

        # copy3
        # num = bin(num)
        # num=num[2:]
        # num = list(num)
        # for i in range(len(num)):
        #     if num[i] == '0':
        #         num[i] ='1'
        #     else:
        #         num[i]='0'
        # num = "".join(num)

        # return int(num,2)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        #copy
# 先“按位加”，也就是异或，在python中为^ #1^0=1 1^1=0(因为要进位) 0^0=0 
# 处理进位，进位就是和，在python中为&，还要左移<<1位  #1&1就要进位再左移
# 循环上述步骤就好了
        # 解析：https://blog.csdn.net/qq_34364995/article/details/80738911
        #     https://blog.csdn.net/liyuanbhu/article/details/51803974
        # mask = 0xffffffff # 是一个负数的补码。都是1
        # while b & mask: #b!=0
        #     a, b = a ^ b, (a & b) << 1

        # return a & mask if b > mask else a

        MAX_INT = 0x7FFFFFFF    #int类型最大的值
        MIN_INT = MAX_INT + 1
        MASK = 0x100000000      #等于2^32,1-32位上都是1
        while b != 0:
            carry = (a & b) << 1    #表示进位
            a = (a ^ b) % MASK  #对其取余则将范围限制在[0,2^32-1]内，也就是int的范围
            b = carry % MASK    #同理
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)    
# python中一直左移是不会溢出的，所以要手动模拟32位int型
#如果小于MAX_INT就不用处理了，如果溢出就要：
#以4位bit为例，从0000-1111，可以表示的范围为[0,15]，如果计算出16那就是溢出了，16是10000，此时的MIN_4BIT为16，取余为0，0000异或1111为1111再取反就是0了，将范围限制在了4位bit的范围内
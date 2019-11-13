class Solution:
    def countDigitOne(self, n: int) -> int:
        # 未看
        # 需要找到数学规律，还得保证代码的逻辑性
        # 1,10-19,21-91,100-199,200-900开始也是200+，1000-1999，2000开始重复，统计
        # 复杂，按照位数统计规律
        # 1 https://mp.weixin.qq.com/s/vKHjt8cu0d_UTH7QistAyA
        # 2、http://www.ishenping.com/ArtInfo/1262302.html
        if n <= 0: return 0

        operator = 1
        count = 0

        while n // operator:
            curr = n % (operator * 10) // operator
            high = n // (operator * 10)
            low = n % (operator)

            # 根据当前位的3种情况，进行计数
            if curr == 1:
                count += high * operator + low + 1
            if curr == 0:
                count += high * operator
            if curr > 1:
                count += (high + 1) * operator

            operator *= 10

        return count
        # 转换为字符统计,超时
        # c=0
        # if n > 0:
        #     for i in range(n+1):
        #         contain_str = "1"
        #         if contain_str in str(i):
        #             for  a in list(str(i)):
        #                 if a=='1':
        #                     c+=1 
        # return c

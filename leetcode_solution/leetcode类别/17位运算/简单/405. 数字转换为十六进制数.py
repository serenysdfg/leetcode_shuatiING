class Solution:
    def toHex(self, num: int) -> str:
        #先转为二进制,然后四个里面1.2.4.88
        d={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        a=[]
        if num<0:
            num = int(''.join([str(1 - int(i)) for i in list(bin(-num)[2:].zfill(32))]), base=2)+1#转化成整数
        elif num==0:
            return '0'
        while num>0:
            m=num//16
            if num%16>=10:
                a.append(d[num%16])
            else:
                a.append(str(num%16))
            num=m
        return ''.join(str(i) for i in a[::-1])
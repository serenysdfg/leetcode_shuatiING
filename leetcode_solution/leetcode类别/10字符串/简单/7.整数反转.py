class Solution:
    def reverse(self, x: int) -> int:
        # x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1]) #字符反转
        # return x if x < 2147483648 and x >= -2147483648 else 0
        #copy2
        # R = 0   #返回值
        # flag = 1 #标记输入值的正负
        # if x<0:
        #     x = abs(x)
        #     flag = -1 #输入是负数
        # while x != 0:
        #     R = R*10+x%10
        #     x = x//10
        # if -2147483647<R< 2147483648:#判断是否越界
        #     return R*flag
        # else:
        #     return 0

        #me  -10)%3 有问题，先变成整数

        flag=0
        if x<0:flag=1
        sum=0
        x=abs(x)
        while x!=0:
            sum=sum*10+(x%10) #-10)%3 有问题，先变成整数
            x//=10  
        if flag==1:sum=sum*(-1)
        if sum>pow(2,31)-1 or sum<-1*pow(2,31):return 0 
        return sum
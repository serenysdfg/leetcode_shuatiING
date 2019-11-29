class Solution:
    def isHappy(self, n: int) -> bool:
        '''. 结果为1则为true;
2. 结果无限循环，这就需要保存计算过的值，当然是使用散列表实现的字典。这里如果使用递归的话很难维护字典，所以最后改为递推'''
        d = {}
        while True:
            l = list(map(int,list(str(n))))  #19:['1','9']
            m = 0
            for i in l:
                m += i**2
            if m in d:
                print(d)
                return False
            if m == 1:
                print(d)
                return True
            d[m] = m #回来了就是循环
            n = m

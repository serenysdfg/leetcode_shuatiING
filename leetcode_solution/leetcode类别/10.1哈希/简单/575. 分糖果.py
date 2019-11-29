class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #lose
        #思考:用set（）函数判断一共有多少种糖果，如果糖果种类数比每个人分的糖果数多，那么可以给妹妹的糖果全是不同种类的，即为总糖果数的一半；如果糖果种类数小于每个人的糖果数，则将所有不同种类的糖果全部分给妹妹，然后用重复的种类凑够妹妹应得的糖果数，即妹妹获得的种类为全部种类
        len1 = len(candies)
        n = len(list(set(candies)))
        if n*2 >= len1: 
            return len1//2
        else :
            return n
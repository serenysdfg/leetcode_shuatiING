'''假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # copy
        flowerbed = [0] + flowerbed + [0]  # 左右各加一个空位置
        for i in range(1, len(flowerbed) - 1):  # 遍历出两端之外的位置
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:  # 遇到连续三个空位置
                flowerbed[i] += 1  # 放一盆花，改变值
                n -= 1  # 花数减一
            if n <= 0:  # 如果花用完了，返回True
                return True
        return False

        # 花没用完，返回False
#         #失败太多忽视 [1,0,0,0,0]
#         i=0
#         count=0
#         m=len(flowerbed )-1
#         if n==0 :return True #先判断  # n==0容易忽视 2忽视了一开始两个0
#         if (len(flowerbed) <3 ):# 也可以插入-忽视
#             if flowerbed[0]==0 and m==0: return True
#             if flowerbed[0]==0 and flowerbed[1]==0 and m==1 :return True
#             else:
#                 return False # 也可以插入-忽视

#         if flowerbed[0]==0 and flowerbed[1]==0 and flowerbed[2]==1:
#             count+=1 #2忽视了一开始两个0和最后
#             i=3
#         while i+2 <len(flowerbed):
#             if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i+2]==0:
#                 i+=2
#                 count+=1
#                 print("count:"+str(count))

#             else:
#                 i+=1
#         if flowerbed[m-2]==1 and flowerbed[m-1]==0 and flowerbed[m]==0:
#             count+=1 #2忽视了一开始两个0和最后
#         if count>=n:
#             return True
#         return False


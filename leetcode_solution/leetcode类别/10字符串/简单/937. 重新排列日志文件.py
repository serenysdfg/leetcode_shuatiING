class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        n = len(logs)
        tmp = []
        res = []
        mm = []
        for i in range(n):
            index = 0
            for j in range(len(logs[i])):  # 每条的字母遍历
                if ' ' == logs[i][j]:
                    index = j + 1  # 获取字母或者数字
                    break
            cc = ord(logs[i][index]) - ord('0')
            if cc >= 0 and cc <= 9:
                tmp.append(logs[i])  # 数字
            else:
                mm.append([logs[i][index:], logs[i][0:index]])  # 分成前后
        mm.sort()
        for i in range(len(mm)):
            res.append(mm[i][1] + mm[i][0])
        for i in range(len(tmp)):
            res.append(tmp[i])

        return res
#         我们借助python中sort函数的关键字完成排序，每一个日志对应一个元组，利用元组的不同位置代表不同优先级，排序优先级为：
# 第一优先级为日志类型，字母为0，数字日志设置为1；
# 第二优先级为日志内容，因此每条日志对应元组的第二个元素放日志内容即可；
# 第三优先级为日志标志符，放在每条日志对应元素的第三个元素位置。

# 由于只有字母日志内部需要排序，因此数字日志对应的元素也可以设置为空


#         #copy
#         def f(log):
#             id_, rest = log.split(" ", 1)
#             return (0, rest, id_) if rest[0].isalpha() else (1,)#是数字(1,) 是字母 (0, rest, id_)还要根据字母，字母日志都排在数字日志之前

#         return sorted(logs, key = f)#


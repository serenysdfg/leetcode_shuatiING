class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dis(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
    #一个一个思考,,
        result = 0
        for i in points:
            record = {}
            for j in points:
                if j != i:
                    distance = dis(i, j)
                    record[distance] = record.get(distance, 0) + 1 #查看每一个对应有几个相同,大于两个计算,要选两个排序c(val,2)*2!

            for val in record.values():
                if val >= 2:
                    result += (val - 1)* val

        return result


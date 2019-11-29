class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # 超时
        #     if not triangle:
        #         return 0
        #     return self._minimumTotal(0, 0, triangle)

        # def _minimumTotal(self, row, col, triangle):
        #     if row + 1 == len(triangle):
        #         return triangle[row][col]

        #     return triangle[row][col] + min(self._minimumTotal(row + 1, col, triangle), self._minimumTotal(row + 1, col + 1, triangle))
        # copy1倒金字塔
        # 两个位置随机，用dp两种情况
        if not triangle:
            return 0

        for row in range(len(triangle) - 1, 0, -1):  # 倒回去
            for col, _ in enumerate(triangle[row - 1]):  # 每一行
                triangle[row - 1][col] += min(triangle[row][col], triangle[row][col + 1])  # 循环所有获取最小，col和自己相同或者+1，加上更小的

        return triangle[0][0]

# copy2
# n = len(triangle)
# if n == 1: return triangle[0][0]
# elif n == 2 : return min(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
# else:
# 	res = []
# 	for i in range(n):
# 		res.append(triangle[i])

# 	res[0] = [triangle[0][0]]
# 	res[1] = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]

# 	for i in range(2,n):
# 		for j in range(i+1):
# 			if j == 0:
# 				res[i][j] = res[i-1][j] + triangle[i][j]
# 			elif j == i:
# 				res[i][j] = res[i-1][-1] + triangle[i][j]
# 			else:
# 				res[i][j] = min(res[i-1][j-1],res[i-1][j]) + triangle[i][j]

# 	return min(res[-1])

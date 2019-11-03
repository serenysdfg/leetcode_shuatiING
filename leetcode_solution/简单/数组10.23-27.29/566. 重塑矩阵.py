输入:
nums =
[[1, 2],
 [3, 4]]
r = 1, c = 4
输出:
[[1, 2, 3, 4]]
解释:
行遍历nums的结果是[1, 2, 3, 4]。新的矩阵是
1 * 4
矩阵, 用之前的元素值一行一行填充新矩阵。

来源：力扣（LeetCode）
链接：https: // leetcode - cn.com / problems / reshape - the - matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        result = []
        if (len(nums[0]) * len(nums) != r * c):  return nums
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if len(res) == c:
                    result.append(res)
                    res = []

                if len(res) < c:
                    res.append(nums[i][j])
                    print(res)
        result.append(res)
        return result

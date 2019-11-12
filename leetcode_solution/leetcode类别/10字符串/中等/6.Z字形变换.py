class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # copy规律除以多少难
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows  ##多个字符串数组
        idx, step = 0, 1  # idx行数+1或者-1

        for x in s:
            res[idx] += x
            if idx == 0:  ## 第一行，一直向下走
                step = 1
            elif idx == numRows - 1:  ## 最后一行了，向上走
                step = -1
            idx += step
        return ''.join(res)  # ['agm', 'bfhln', 'ceik', 'dj']
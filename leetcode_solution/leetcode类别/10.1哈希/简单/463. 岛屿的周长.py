class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #copy
        # 重点:每一个陆地单元格的周长为4，当两单元格上下或者左右相邻时，令周长减2(重叠的去掉多算了两次) ,只需要考虑左边和上边
        h = len(grid)
        w = len(grid[0]) 
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    # 因为x+1还在后面，所以不需要考虑，即只需要考虑左边和上边，因为循环已经出现过该点了
                    if x > 0 and grid[x - 1][y]:   
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans

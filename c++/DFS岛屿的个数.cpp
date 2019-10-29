BFS : 所有相邻节点一步步
          DFS : 深度，不行再退回
                /**
 * DFS核心伪代码
 * 前置条件是visit数组全部设置成false
 * @param n 当前开始搜索的节点
 * @param d 当前到达的深度，也即是路径长度
 * @return 是否有解
 */
                bool
                DFS(Node n, int d)
{
    if (d == 4)
    { //路径长度为返回true，表示此次搜索有解
        return true;
    }

    for (Node nextNode in n)
    { //遍历跟节点n相邻的节点nextNode，
        if (!visit[nextNode])//未访问过的节点才能继续搜索
        { 
            visit[nextNode] = true; //例如搜索到V1了，那么V1要设置成已访问
            /
            if (DFS(nextNode, d + 1))//如果搜索出有解
            {  return true;        //例如到了V6，找到解了，你必须一层一层递归的告诉上层已经找到解  }
          
            visit[nextNode] = false;  //重新设置成未访问，因为它有可能出现在下一次搜索的别的路径中
        }
        //到这里，发现本次搜索还没找到解，那就要从当前节点的下一个节点开始搜索。
    }
    return false; //本次搜索无解
}
// 6.OJ题目
// 题目分类来自网络：
// sicily：1019 1024 1034 1050 1052 1153 1171 1187
// pku：1088 1176 1321 1416 1564 1753 2492 3083 3411
###########################################
// 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

//     示例 1 :

//     输入 : 11110 11010 11000 00000

//     输出 : 1

//     示例 2 :

//     输入 : 11000 11000 00100 00011

//     输出 : 3 class Solution
{
  public:
    void DFS(vector<vector<char>> &grid, vector<vector<int>> &visited, int i, int j)
    {
        if (i > 0 && grid[i - 1][j] == '1' && visited[i - 1][j] == 0)
        {
            visited[i - 1][j] = 1;
            DFS(grid, visited, i - 1, j);
        }
        if (j > 0 && grid[i][j - 1] == '1' && visited[i][j - 1] == 0)
        {
            visited[i][j - 1] = 1;
            DFS(grid, visited, i, j - 1);
        }
        int n1 = grid.size();
        int n2 = grid[0].size();
        if (i < n1 - 1 && grid[i + 1][j] == '1' && visited[i + 1][j] == 0)
        {
            visited[i + 1][j] = 1;
            DFS(grid, visited, i + 1, j);
        }
        if (j < n2 - 1 && grid[i][j + 1] == '1' && visited[i][j + 1] == 0)
        {
            visited[i][j + 1] = 1;
            DFS(grid, visited, i, j + 1);
        }
    }
    int numIslands(vector<vector<char>> &grid) //vector<vector<char>矩阵
    {
        int n1 = grid.size(); //横
        if (n1 == 0)
            return 0;
        int n2 = grid[0].size(); //竖
        if (n2 == 0)
            return 0;
        vector<vector<int>> visited(n1, vector<int>(n2, 0)); //visited(n1, vector<int>(n2, 0));标志变量0水
        int num = 0;
        for (int i = 0; i < n1; i++)
        {
            for (int j = 0; j < n2; j++)
            {
                if (grid[i][j] == '1' && not visited[i][j]) //岛屿没有看过
                {
                    num++;
                    DFS(grid, visited, i, j); //周边的都遍历
                }
            }
        }
        return num;
    }
};
#include <iostream> //1364
#include <algorithm>
#include <set> 
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
 
using namespace std;
 
struct _bomb 
{
    int v;
    int d;
}bomb[1001];//bomb结构体，v空间，d破坏力 
 
int dp[1001];
 
int main()
{
    int s;//空间 
    int c;//炸药 个数 
 
 
    while(cin >> s >> c)
    {
        memset(dp,0,sizeof(dp));//数组初始化 
        for(int i = 0; i < c; i++)
            cin >> bomb[i].v>> bomb[i].d; // 录入数据 
 
        for(int i = 0; i < c; i++)
            for(int j = s; j >= bomb[i].v; j--)
                dp[j] = max(dp[j],dp[j - bomb[i].v]+bomb[i].d);
         
        cout<<dp[s]<<endl;
    }
         
    return 0;
}

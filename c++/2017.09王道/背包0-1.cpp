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
}bomb[1001];//bomb�ṹ�壬v�ռ䣬d�ƻ��� 
 
int dp[1001];
 
int main()
{
    int s;//�ռ� 
    int c;//ըҩ ���� 
 
 
    while(cin >> s >> c)
    {
        memset(dp,0,sizeof(dp));//�����ʼ�� 
        for(int i = 0; i < c; i++)
            cin >> bomb[i].v>> bomb[i].d; // ¼������ 
 
        for(int i = 0; i < c; i++)
            for(int j = s; j >= bomb[i].v; j--)
                dp[j] = max(dp[j],dp[j - bomb[i].v]+bomb[i].d);
         
        cout<<dp[s]<<endl;
    }
         
    return 0;
}

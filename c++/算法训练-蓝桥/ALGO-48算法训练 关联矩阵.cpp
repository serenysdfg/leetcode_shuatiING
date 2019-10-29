#include <iostream>
#include <cstdio>
using namespace std;
int ans[101][1001];
int main()
{
    int n,m;
    int a,b;
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d",&a,&b);
        ans[a][i] = 1;
        ans[b][i] = -1;
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m-1;j++)
        {
            printf("%d ",ans[i][j]);
        }
        printf("%d\n",ans[i][m]);
    }
    return 0;
}


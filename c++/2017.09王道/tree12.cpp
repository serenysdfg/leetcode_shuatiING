#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
#define ll long long
const int maxn=1e5+5;
const int INF=0x3f3f3f3f;

struct Edge
{
    int v,l;
    int next;
} edge[maxn<<2];

int vit[maxn],d[maxn];
int head[maxn],k;
int node,ans;

void init()
{
    k=0;
    memset(head,-1,sizeof(head));
}

void addedge(int u,int v,int l)
{
    edge[k].v=v;
    edge[k].l=l;
    edge[k].next=head[u];
    head[u]=k++;

    edge[k].v=u;
    edge[k].l=l;
    edge[k].next=head[v];
    head[v]=k++;
}

void dfs(int u,int t)
{
    for(int i=head[u]; i!=-1; i=edge[i].next)
    {
        int v=edge[i].v;
        if(vit[v]==0)
        {
            vit[v]=1;
            d[v]=t+edge[i].l;
            if(d[v]>ans)
            {
                ans=d[v];
                node=v;
            }
            dfs(v,d[v]);
        }
    }
}

int main()
{
    //freopen("in.txt","r",stdin);
    init();
    int l,r,len;
    while(scanf("%d%d%d",&l,&r,&len)==3)
    {
        addedge(l,r,len);
    }

    memset(vit,0,sizeof(vit));
    vit[1]=1;
    ans=0;
    dfs(1,0);

    memset(vit,0,sizeof(vit));
    vit[node]=1;
    ans=0;
    dfs(node,0);

    printf("%d\n",ans);

    return 0;
}

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<queue>
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

void bfs(int p)
{
    queue<int>q;
    vit[p]=1;
    q.push(p);
    while(!q.empty())
    {
        int u=q.front();
        q.pop();
        for(int i=head[u]; i!=-1; i=edge[i].next)
        {
            int v=edge[i].v;
            if(vit[v]==0)
            {
                d[v]=d[u]+edge[i].l;
                vit[v]=1;
                q.push(v);
                if(d[v]>ans)
                {
                    ans=d[v];
                    node=v;
                }
            }
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
    memset(d,0,sizeof(d));
    ans=0;
    bfs(1);

    memset(vit,0,sizeof(vit));
    d[node]=0;
    ans=0;
    bfs(node);

    printf("%d\n",ans);

    return 0;
}

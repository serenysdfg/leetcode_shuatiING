#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <queue>
#include <cstring>

/*
简单的单源最短路问题
朴素SPFA 
一组错、猜测算法出错 
*/ 


using namespace std;

const int maxN=100000, maxM=300000;
int N, m=0, M, H[maxN], D[maxM], F[maxN]={};


struct Edge{
	int z, y, w;
}E[maxM];

int  Relax(int &w, int m){
	return m<w?(w=m):0;
}

void addE(int x, int y, int w){
	E[++m].y = y;
	E[m].w = w;
	E[m].z = H[x];
	H[x] = m;
}

/*void SPFA(int x){
	bool F[maxN]={};
	queue<int> Q;
	int y;
	for (memset(D, 0x7f, sizeof(D)), D[x]=0, F[x]=1, Q.push(x); !Q.empty(); F[x]=0,Q.pop())
		for (int i=H[x=Q.front()]; i; i=E[i].z)
			if (Relax(D[y=E[i].y], E[i].w+D[x]) && !F[y]){
				F[y] = 1;
				Q.push(y);
			}
}*/

void SPFA(int S)
{
	memset(D, 0x7f, sizeof(D));
    D[S]=0;
    F[S]=true;

    deque <int> q;
    for(q.push_back(S);!q.empty();)
    {
        int x=q.front();
        q.pop_front();
        for(int k=H[x];k!=-1;k=E[k].z)
        {
            int y=E[k].y;
            if(D[y]>D[x]+E[k].w)
            {
                D[y]=D[x]+E[k].w;
                if(!F[y])
                {
                    F[y]=true;
                    if(!q.empty())
                    {
                        if(D[y]>D[q.front()])
                            q.push_back(y);
                        else
                            q.push_front(y);
                    }
                    else
                        q.push_back(y);
                }
            }
        }
        F[x]=false;
    }
    return ;
}


int main(){
	cin>> N>> M;
	for(int i=0; i<maxN; i++) H[i]=-1;
	for (int i=1; i<=M; i++){
		int u, v, l;
		scanf("%d%d%d", &u, &v, &l);
		addE(u, v, l);
	}
	SPFA(1);
	for (int i=2; i<=N; i++){
		printf("%d\n", D[i]);
		//cout<< D[i]<< endl;
	}
	return 0;
}
C
#include<stdio.h>
#include<string.h>
#define inf 100000
struct In{
    int e;
    int w;
    int next;
}map[200010];
int dis[20010],Q[20010];
int vis[20010],head[20010];
void SPFA(int n){
    int i,j,front,rear,temp;
    for(i=1;i<=n;i++){
        dis[i]=inf;
    }
    dis[1]=0;vis[1]=1;
    front=0;rear=1;
    Q[front]=1;
    while(front<rear){
        temp=Q[front++];
        vis[temp]=0;
        j=head[temp];
        while(j>0){
            if(dis[map[j].e]>map[j].w+dis[temp]){
                dis[map[j].e]=map[j].w+dis[temp];
                if(!vis[map[j].e]){
                    Q[rear++]=map[j].e;
                    vis[map[j].e]=1; 
                }
            }
            j=map[j].next;
        }
    }
}
int main(){
    int n,m,i,j,a,b,val;
    while(~scanf("%d%d",&n,&m)){
        memset(Q,0,sizeof(Q));
        memset(head,0,sizeof(head));
        memset(vis,0,sizeof(vis));
        for(i=1;i<=m;i++){
            scanf("%d%d%d",&a,&b,&val);
            map[i].e=b;
            map[i].w=val;
            map[i].next=head[a];
            head[a]=i;
        }
        SPFA(n);
        for(i=2;i<=n;i++){
            printf("%d\n",dis[i]);
        }
    }
    return 0;
}


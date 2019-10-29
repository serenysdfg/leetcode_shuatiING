#include<stdio.h>
#include<stdlib.h>
#include<string.h>


typedef struct Node//树形结构 
{
    int to;
    int next;
}Node;

#define N 100020

int max(int a, int b)//返回较大的值 
{
    return a > b ? a : b;
}


int on[N], off[N];

int rel[N];
Node relBus[2 * N];
int relBusTop = 1;

int queue[N] = {1};
int qStart = 0, qEnd = 1;

int checked[N] = {0, 1};

int ser[N];
int sp = 0;

int main(void)
{
    int n, i, j;
    
    scanf("%d", &n);
    for(i = 1; i <= n; i++)
    {
        scanf("%d", &on[i]);
        off[i] = 0;
    }
    
    for(i = 0; i < n - 1; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        
        relBus[relBusTop].to = b;
        relBus[relBusTop].next = rel[a];
        rel[a] = relBusTop++;
        
        relBus[relBusTop].to = a;
        relBus[relBusTop].next = rel[b];
        rel[b] = relBusTop++;
    }

    while(qStart < qEnd)
    {
    	int now = queue[qStart++];
    	ser[sp++] = now;
    	int p = rel[now];
    	while(p > 0)
    	{
    		int son = relBus[p].to;
    		if(checked[son] == 0)
    		{
    			queue[qEnd++] = son;
    			checked[son] = 1;
    		}
    		p = relBus[p].next;
    	}
    }
    
    for(i = n - 1; i >= 0; i--)
    {
    	int son = ser[i];
    	int p = rel[son];
    	
    	while(p > 0)
    	{
    		int father = relBus[p].to;
    		
    		on[father] += off[son];
    		off[father] += max(on[son], off[son]);
    		p = relBus[p].next;
    	}
    }
    
    printf("%d", max(on[1], off[1]));
    return 0;
}


#include<stdio.h>
const int NO=1000005;
int dp[NO][2];
int du[NO];
int first[NO],next[NO],v[NO],num=1;
bool mark[NO];
int n,a;
int t[NO],tip,top;
int max(int a,int &b){return a>b?a:b;}
void input(int &num)
{
	num=0;
	char ch=getchar();
	while(ch<'0'||'9'<ch)
		ch=getchar();
	while('0'<=ch&&ch<='9')
	{
		num=10*num+ch-'0';
		ch=getchar();
	}
}
void add(int &a,int &b)
{
	v[num]=b;
	next[num]=first[a];
	first[a]=num++;
	v[num]=a;
	next[num]=first[b];
	first[b]=num++;
}
int work()
{
	int i;
	while(tip<top)
	{
		a=t[tip++];
		mark[a]=1;
		for(i=first[a];i!=-1;i=next[i])
			if(mark[v[i]])
			{
				dp[a][0]+=max(dp[v[i]][0],dp[v[i]][1]);
				dp[a][1]+=dp[v[i]][0];
			}
			else if(--du[v[i]]==1)
				t[top++]=v[i];
	}
	return max(dp[a][0],dp[a][1]);
}
int main()
{
	int i,a,b;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		input(dp[i][1]),first[i]=-1;
	for(i=1;i<n;i++)
		input(a),input(b),add(a,b),du[a]++,du[b]++;
	for(i=1;i<=n;i++)
		if(du[i]==1)
			t[top++]=i;
	printf("%d\n",work());
	return 0;
}


#include<stdio.h>

int main()
{
	int m,s,n;
	int sum=0;
	int i,j,l;
	int a[200][200],b[200][200],c[200][200];
	scanf("%d%d%d",&m,&s,&n);
	for(i=0;i<m;i++)
	{
		for(j=0;j<s;j++)
		scanf("%d",&a[i][j]);
	}
	for(i=0;i<s;i++)
	{
		for(j=0;j<n;j++)
		scanf("%d",&b[i][j]);
	}
	//以上输入 
	
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			for(l=0;l<s;l++)
			{
				sum+=(a[i][l]*b[l][j]);//变化的放在里面，，重要 
			}
			c[i][j]=sum;
			sum=0;
		}
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		printf("%d ",c[i][j]);
		printf("\n");
	}
	return 0;
}


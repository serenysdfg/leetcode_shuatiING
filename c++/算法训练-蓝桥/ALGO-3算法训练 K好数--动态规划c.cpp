#include<stdio.h>
int main()
{
	int i;
	int k;		//������
	int l;		//λ��
	long long ka[100];		//ǰ
	long long kb[100];		//��ǰ
	long long cont=0;		//����
	scanf("%d%d",&k,&l);
	kb[0]=ka[0]=0;
	for(i=1;i<k;i++)
	{
		kb[i]=ka[i]=1;
	}
	for(i=2;i<=l;i++)
	{
		int j;
		for(j=0;j<k;j++)
		{
			int m=0;
			for(m=0;m<k;m++)
			{
				if(m<j-1 || m>j+1)
					kb[j]+=ka[m];
			}
			
		}
		for(j=0;j<k;j++)
		{
			ka[j]=kb[j];
			ka[j]=kb[j]%1000000007;
		}
	}
	while(k--)
	{
		cont+=ka[k];
		cont=cont%1000000007;
	}
	printf("%I64d\n",cont);
	return 0;
}


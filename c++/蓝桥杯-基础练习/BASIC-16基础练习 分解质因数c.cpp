#include<stdio.h>
#include<math.h>
int main()
{
	long int b,i,k,m,n,w = 0;
	scanf("%ld%ld",&m,&n);
	for(i = m;i<=n;i++)
	{
		printf("%ld=",i);
		b = i;k = 2;
		while(k<=sqrt(i))
		{
			if(b%k==0) //��ʾ��ʽ 
			{
				b = b/k;
				if(b>1)
				{
					printf("%ld*",k);continue;
				}   
				if(b==1) printf("%ld\n",k);
			}
			k++;
		}
		if(b>1&&b<i) printf("%ld\n",b);//���һ���� 
		if(b==i)
		{
			printf("%d\n",i);w++;//�����Ǹ��� 
		}     
	}
	return 0;
}

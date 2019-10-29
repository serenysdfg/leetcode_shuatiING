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
			if(b%k==0) //显示公式 
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
		if(b>1&&b<i) printf("%ld\n",b);//最后一个数 
		if(b==i)
		{
			printf("%d\n",i);w++;//还是那个数 
		}     
	}
	return 0;
}

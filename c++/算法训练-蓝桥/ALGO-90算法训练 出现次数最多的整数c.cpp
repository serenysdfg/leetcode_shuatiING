#include <stdio.h>
int main()
{
	int n,i,j,t,max=1,num=0;
	scanf("%d",&n);
	if(n>0)
	{
		int a[n];
		for(i=0;i<n;i++)
			scanf("%d",a+i);
		j=num=a[0];
		t=1;
		for(i=1;i<n;i++)
			if(a[i]==j){
				++t;
				if(t>max)	max=t;num=a[i];
			}
			else{	t=1;	j=a[i];	}
	printf("%d",num);
	}

	return 0;
}


#include<stdio.h>
#include<string.h>
//假如有一半以上的芯片同意了本芯片为好芯片的话，则本芯片为一个好的芯片。下面是本渣渣的AC代码。
int main()
{
	int a[50][50];
	int i,j,n,s;
	scanf("%d",&n);
 	for(j=0;j<n;j++)
	   for(i=0;i<n;i++)
	   		scanf("%d",&a[i][j]);
	for(j=0;j<n;j++){
		s=0;
		for(i=0;i<n;i++)
			s=s+a[j][i];
		if(s>n/2.0)
			printf("%d ",j+1);
		}
	return 0;
}

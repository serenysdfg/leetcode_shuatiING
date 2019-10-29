#include<stdio.h>
int main(){
	int a[11],i,j,t;
	for(i=0;i<=10;i++) a[i]=0;//初始化伟0
	for(i=1;i<=5;i++){
		scanf("%d",&t);
		a[t]++;//进行计数 
	} 
	for(i=0;i<=10;i++){
		for(j=1;j<=a[i];j++){
			printf("%d",i);
		
		}
	
	} 
	getchar();getchar();
	return 0;
}

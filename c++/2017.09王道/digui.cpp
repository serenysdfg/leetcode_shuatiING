#include<stdio.h>
#include<string.h>
Long long F(int num){
	if(num==1) return 2;//����Ϊ1ʱ����2
	else 
		return 3*F(num-1)+2;//����ݹ����F��num-1�� 
}
int main(){
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		printf("%lld\n",F(n));//����� 
	}
	return 0; 
} 

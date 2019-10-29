#include<stdio.h>
#include<string.h>
Long long F(int num){
	if(num==1) return 2;//参数为1时返回2
	else 
		return 3*F(num-1)+2;//否则递归调用F（num-1） 
}
int main(){
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		printf("%lld\n",F(n));//输出答案 
	}
	return 0; 
} 

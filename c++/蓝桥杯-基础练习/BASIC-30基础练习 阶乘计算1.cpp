#include<stdio.h> 
#include<string.h> 
#define MAX 3000 
int main() {
	int a[MAX],i,j,n; 
	int c=0; //进位
	int s; 
	memset(a,0,sizeof(a));   //初始化
	scanf("%d",&n); 
	a[0]=1; 
	for(i=2;i<=n;i++){//乘数竖起来 { 
		for(j=0;j<MAX;j++)  //j<MAX 
		{ 
			s=a[j]*i+c;  //每一位相乘 
			a[j]=s%10;  //剩余 
			c=s/10;  //进位，，得到一个答案数组 
		} 
	} 
	for(i=MAX-1;i>=0;i--) //从第一个不为零的开始，a[i]最高位 
		{if(a[i]) break;} 
	for(j=i;j>=0;j--)
		{	printf("%d",a[j]); 	}		
	return 0; 
}


/*
算法描述
　　n!可能很大，而计算机能表示的整数范围有限，需要使用高精度计算的方法。使用一个数组A来表示一个大整数a，A[0]表示a的个位，A[1]表示a的十位，依次类推。
　　将a乘以一个整数k变为将数组A的每一个元素都乘以k，请注意处理相应的进位。
　　首先将a设为1，然后乘2，乘3，当乘到n时，即得到了n!的值。
输入格式
　　输入包含一个正整数n，n<=1000。
输出格式
　　输出n!的准确值。
样例输入10输出
3628800
*/


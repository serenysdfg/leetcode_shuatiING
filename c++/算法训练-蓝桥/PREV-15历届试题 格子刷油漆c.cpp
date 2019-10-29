/*
样例输入
2
样例输出
24
样例输入
3
样例输出
96
*/
#include <stdio.h>  
long long a[1001],b[1001],sum;  
#define NUM 1000000007 
int main()  
{  
    int i,n;  
    scanf("%d",&n);  
    b[1]=1;  
    for (i=2;i<=n;i++)  
        b[i]=(b[i-1]*2%NUM);  
    a[1]=1;a[2]=6;  
    for (i=3;i<=n;i++)  
        a[i]=(2*a[i-1]+b[i]+4*a[i-2])%NUM;  
    sum=4*a[n];  
    for (i=2;i<n;i++)  
        sum=((sum+8*b[n-i]*a[i-1]%NUM)%NUM+(8*a[n-i]*b[i-1])%NUM)%NUM;  
    printf("%I64d\n",sum);  
    return 0;  
}


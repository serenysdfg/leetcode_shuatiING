#include<cstdio>
#include<iostream>
#include<cstring>
 using namespace std;
 int a[101][101];
 int c[101][101];
 int ans[101][101];
 int main()
 {
     int l,m,n;
     scanf("%d%d",&n,&m);//A的阶数和要求的幂数
     for(int i=1;i<=n;i++)
       for(int j=1;j<=n;j++)
         scanf("%d",&a[i][j]);//输入 
     memset(ans,0,sizeof(ans)); //memset(ans,0,sizeof(ans)) 
     for(int i=1;i<=n;i++) ans[i][i]=1;//单位矩阵 
     for(int k=1;k<=m;k++)  //几次幂 
     {   memset(c,0,sizeof(c));
         for(int i=1;i<=n;i++)
		 	for(int j=1;j<=n;j++)
			 	for(int l=1;l<=n;l++)
				 	c[i][j]+=ans[i][l]*a[l][j];
					//第i行j列的值为a的第i行上的n个数和b的第j列上的n个数对应相乘之和，
                    //其中n为a的列数，也是b的行数，a的列数和b的行数相等 
         for(int i=1;i<=n;i++)
		 	for(int j=1;j<=n;j++)
			 	ans[i][j]=c[i][j];  //暂时存储 
     }
     for(int i=1;i<=n;i++)
     {
         for(int j=1;j<n;j++)
			 printf("%d ",ans[i][j]);
         printf("%d\n",ans[i][n]);
     }
     return 0;
 }

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
     scanf("%d%d",&n,&m);//A�Ľ�����Ҫ�������
     for(int i=1;i<=n;i++)
       for(int j=1;j<=n;j++)
         scanf("%d",&a[i][j]);//���� 
     memset(ans,0,sizeof(ans)); //memset(ans,0,sizeof(ans)) 
     for(int i=1;i<=n;i++) ans[i][i]=1;//��λ���� 
     for(int k=1;k<=m;k++)  //������ 
     {   memset(c,0,sizeof(c));
         for(int i=1;i<=n;i++)
		 	for(int j=1;j<=n;j++)
			 	for(int l=1;l<=n;l++)
				 	c[i][j]+=ans[i][l]*a[l][j];
					//��i��j�е�ֵΪa�ĵ�i���ϵ�n������b�ĵ�j���ϵ�n������Ӧ���֮�ͣ�
                    //����nΪa��������Ҳ��b��������a��������b��������� 
         for(int i=1;i<=n;i++)
		 	for(int j=1;j<=n;j++)
			 	ans[i][j]=c[i][j];  //��ʱ�洢 
     }
     for(int i=1;i<=n;i++)
     {
         for(int j=1;j<n;j++)
			 printf("%d ",ans[i][j]);
         printf("%d\n",ans[i][n]);
     }
     return 0;
 }

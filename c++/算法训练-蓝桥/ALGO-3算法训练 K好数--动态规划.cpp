#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop 
��������
���һ����Ȼ��N��K���Ʊ�ʾ����������ڵ���λ���������ڵ����֣���ô���Ǿ�˵�������K��������LλK��������K��������Ŀ������K = 4��L = 2��ʱ������K����Ϊ11��13��20��22��30��31��33 ��7�������������Ŀ�ܴ������������1000000007ȡģ���ֵ��
�����ʽ
�������������������K��L��
�����ʽ
���һ����������ʾ�𰸶�1000000007ȡģ���ֵ��
��������
4 2
�������
7
���ݹ�ģ��Լ��
����30%�����ݣ�KL <= 106��
����50%�����ݣ�K <= 16�� L <= 10��
����100%�����ݣ�1 <= K,L <= 100��
*/
#include<stdio.h>  
int main()  
{  
    int i;  
    int k;      //������  
    int l;      //λ��  
    long long ka[100];      //ǰ  
    long long kb[100];      //��ǰ  
    long long cont=0;       //����  
    scanf("%d%d",&k,&l);  
    kb[0]=ka[0]=0;  
    for(i=1;i<k;i++)  
    {  
        kb[i]=ka[i]=1;  
    }  
    for(i=2;i<=l;i++)  
    {  
        int j;  
        for(j=0;j<k;j++)  
        {  
            int m=0;  
            for(m=0;m<k;m++)  
            {  
                if(m<j-1 || m>j+1)  
                    kb[j]+=ka[m];  //�����������ڵ���ϵĸ��� 
            }  
              
        }  
        for(j=0;j<k;j++)  
        {  
            ka[j]=kb[j];  
            ka[j]=kb[j]%1000000007;  
        }  
    }  
    while(k--)  
    {  
        cont+=ka[k];  
        cont=cont%1000000007;  
    }  
    printf("%I64d\n",cont);  
    return 0;  
}  
/*

int main(int argc,char **argv){
	int k,l;
	cin>>k>>l; //lλk�������� 
	long long table[100][100]; //�� 
	for(int i=0;i<k;i++){
		table[0][i]=1ll; //?????1+ll��long long 
	}
	table[0][0] =011; //??
	for(int i=1;i<l;i++){   //1-lλ 
		for(int j=0;j<k;j++){//0-k-1ѭ������ 
			long long x=0;
			for(int y=0;y<k;y++){
				if(y!=j+1 && y!=j-1){
					x+=table[i-1][y];
				} 
				
			}
			table[i][j]=x%1000000007ll;		
		}
	} 
	long long count=0;
	for(int i=0;i<k;i++){
		count+=table[l-1][i];
	}
	cout<<(count%1000000007ll);
	return 0;
}*/
/* 
int main(int argc, char** argv) {
	int k,l;
	cin>>k>>l;
	long long table[100][100];
	for(int i=0;i<k;i++)
	{
		table[0][i]=1ll;
	}
	table[0][0]=0ll;
	for(int i=1;i<l;i++)
	{
		for(int j=0;j<k;j++)
		{
			long long  x=0;
			for(int y=0;y<k;y++)
			{
				if(y!=j+1 && y!=j-1)
				{
					x+=table[i-1][y];
				}
			}
			table[i][j]=x%1000000007ll;
		}
	}
	long long count=0;
	for(int i=0;i<k;i++)
	{
		count+=table[l-1][i];
	}
	cout<<(count%1000000007ll);
	return 0;
}

*/


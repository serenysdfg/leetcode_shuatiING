/*
问题描述
给定一个序列，每次询问序列中第l个数到第r个数中第K大的数是哪个。
输入格式
第一行包含一个数n，表示序列长度。
第二行包含n个正整数，表示给定的序列。
第三个包含一个正整数m，表示询问个数。
接下来m行，每行三个数l,r,K，表示询问序列从左往右第l个数到第r个数中，从大往小第K大的数是哪个。序列元素从1开始标号。
输出格式
总共输出m行，每行一个数，表示询问的答案。
样例输入
5
1 2 3 4 5
2
1 5 2
2 3 2
样例输出
4
2

*/

#include<iostream>
#include<cstdio>
#include<algorithm> 
#include<cstring>
using namespace std;
bool cmp(int x,int y){
	return x>y;
}
int main(){
    int N,m;//N表示序列长度 ,m示询问的个数 
    int l,r,K;//表示查询数列从第l个到第r个数之间 ，第K大的数是多少 
    scanf("%d",&N);
    int a[N],b[N],flag[N];/*数组b用来存放a中从第l个到第r个数，即查询区间*/
    for(int i=0;i<N;i++){
        scanf("%d",&a[i]);
        /*记录原序*/
        flag[i] = a[i];
    }
    scanf("%d",&m);//录入询问个数 
    int result[m];//c数组用来存放查询结果:应该用m个元素 
    for(int s=0;s<m;s++){//几轮 
        scanf("%d%d%d", &l, &r, &K);    
        for(int j = 0, i = l-1; i < r; i++){/*把a数组中从第l个到第r个数赋给数组b*/ 
            b[j++] = a[i];
        }
        /*将b数组冒泡降序*/ 
        sort(b,b+r-l,cmp);
      
        /*按条件将答案存入数组*/
        result[s] = b[K-1];
        /*a数组返回原序*/
        for(int i=0;i<N;i++){
            a[i] = flag[i];
        }
    }
    /*按条件输出*/ 
    for(int j=0;j<m;j++){
        printf("%d\n",result[j]);
    }
}

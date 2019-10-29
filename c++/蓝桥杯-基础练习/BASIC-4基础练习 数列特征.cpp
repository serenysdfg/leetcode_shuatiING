/*问题描述
给出n个数，找出这n个数的最大值，最小值，和。
输入格式
第一行为整数n，表示数的个数。
第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。???
输出格式
输出三行，每行一个整数。第一行最大值，第二行表最小值，第三行表示这些数的和。
*/
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int main(){
    int n;
    while(cin>>n){
        int a[10005];
        int sum=0;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        sort(a,a+n);//排序从小到大 
        cout<<a[n-1]<<endl<<a[0]<<endl<<sum<<endl;
    }
    return 0;
}
/*
#include<iostream>
using namespace std;
int main(){
	const int MAXN=10001;
	int n,a[MAXN],max,min,sum=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
		sum+=a[i];
	} 
	for(int i=0;i<n-1;i++){
		if(a[i+1]<a[i]){
			int temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;		
		}
	}
	max=a[n-1];
	for(int i=n-1;i>0;i--){
		if(a[i-1]>a[i]){
			int temp=a[i];
			a[i]=a[i-1];
			a[i-1]=temp;		
		}
	}
	min=a[0];
	cout<<max<endl<<min<<endl <<sum<<endl;
	return 0;
} 
*/

/*
问题描述
给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。
如果a在数列中出现了，输出它第一次出现的位置(位置从1开始编号)，否则输出-1。
样例输入
6
1 9 4 8 3 9
9
样例输出
2
*/
#include<iostream>
using namespace std;
int main(){
	const int MAXN=10001;
	int n,a[MAXN],f,ans=-1;//,ans=-1提前声明 
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	} 
	cin>>f;

	for(int i=0;i<n;i++){
		if(f==a[i]){
			ans=i+1;
		
		}
	}
	cout<<ans;
	return 0;
}

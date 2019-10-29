#include<stdio.h>
int main(){
	int a[10000],n,max,ans;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	max=a[0];ans=0;
	for(int i=1;i<n;i++){
		if(a[i]>a[i-1]){
			max=a[i];
			ans=i;
		}
	}
	printf("%d %d",max,ans);
	
	
	return 0;
}


/*
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int main(){
	int n,a[1000],max,ans;
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>a[i];
	max=a[0];ans=0;
	for(int i=1;i<n;i++){
		if(a[i]>max){
			max=a[i];
			ans=i;
		}
	}
	cout<<max<<" "<<ans;
	return 0;
}

*/

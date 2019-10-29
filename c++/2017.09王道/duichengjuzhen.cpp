#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	string a;
	cin>>a;
	int l,n1,n2,n3;
	l=a.size();
	if(l%2){
		n1=(l-4)/2+1;
	}
	else n1=(l-5)/2+1;
	n2=l-n1*2+2;
	for(int i=0;i<n1-1;i++){
		cout<<a[i];
		if(l%2){
			for(int i=0;i<3;i++){
				cout<<" "; 
			}
		
		}
		else cout<<" "<<" ";
		cout<<a[l-1-i];
		cout<<"\n"	;
	}
	if(l%2){
		for(int i=n1-1;i<n1+5;i++){
			cout<<a[i];
		}
	}
	else{
			for(int i=n1-1;i<n1+4;i++){
				cout<<a[i];
			}
	}
	
	
}

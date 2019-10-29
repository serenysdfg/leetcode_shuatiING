#include<iostream>
#include<cstring>
using namespace std;
int main(){
	string a="asdhuydfhuyhuyf";
	int m=0;
	int l=a.size();
	string b="huy";
	int start=0,g=0;	
	int pos=a.find(b,start);
	while(pos!=-1) {
		cout<<pos<<endl;
		m++;
		pos=a.find(b,pos+1);				
	}
	cout<<m<<endl;
	
		
	
	
} 

/*
*/

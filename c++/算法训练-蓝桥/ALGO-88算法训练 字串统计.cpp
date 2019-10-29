#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
int main(){
	string a;
	int len,sum=0,u=0;
	getline(cin,a);
	len=a.size();
	for(int i=len-1;i>=0;i--){
		sum+=pow(2,u)*(a[i]-'0');
		u++;
		
		
	} 
	cout<<sum<<endl;
	
	
	return 0;
}

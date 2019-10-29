#include<iostream>
#include<cstring>
using namespace std;

int main(){
	string str1,str2;
	int len;
	char a;
	getline(cin,str1);
	cin>>a;
	len=str1.size();
	for(int i=0;i<len;i++){
		if(str1[i]!=a){
			str2+=str1[i];
		}
	}
	cout<<str2<<endl;
	return 0;
}


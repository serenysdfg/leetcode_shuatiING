#include<iostream>
#include<string>
#include<math.h> 

using namespace std;
int main(){
	string s;
	int a=0;
	while(cin>>s){
		int leth=s.length();
		long long sum=0;
		while(leth){
			if(s[leth-1]>='A'&&s[leth-1]<='F'){
			
				sum+=(s[leth-1]-'7')*pow(16,a++);
				//cout<<sum<<endl;
			}
			else{
				sum+=(s[leth-1]-'0')*pow(16,a++);
				//cout<<sum<<endl;
			}
			leth--;
		}
		cout<<sum<<endl;		
	}
	return 0;
} 

/*
string s;
cin>>s //��ȡ����
s[i] 
�뷨��1ǰ���һ�δ�*16 sum=sum*16+s[i]-'A'+10;,���߳���16�ļ��� 
2����f��1-9��a--f
3long long sum 

*/

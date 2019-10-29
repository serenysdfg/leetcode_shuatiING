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
cin>>s //获取输入
s[i] 
想法：1前面的一次次*16 sum=sum*16+s[i]-'A'+10;,或者乘以16的几次 
2分类f，1-9，a--f
3long long sum 

*/

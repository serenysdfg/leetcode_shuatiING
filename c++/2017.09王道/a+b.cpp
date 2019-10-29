#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int64 a,b;
int main(){
	char s1[20],s2[20] ;
	while(scanf("%s%s",&s1,&s1)!=EOF){
	
		a=b=0;
		int len1,len2;
		len1=strlen(s1);
		len2=strlen(s2);
		for(int i=0;i<len1;i++){
			if(s1[i]>='0'&&s1[i<='9'])
				a=a*10+s1[i]-'0';
		}
		if(s2[0]='-' )  a=-a;
		for(int i=0;i<len2;i++){
			if(s2[i]>='0'&&s2[i<='9'])
				b=b*10+s2[i]-'0';
		}
		if(s2[0]='-' )  b=-b;		
		printf("%I64d",a+b);
		
		
	}
	return 0;
} 

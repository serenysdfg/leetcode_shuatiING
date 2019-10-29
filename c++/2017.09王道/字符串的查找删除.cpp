#include<stdio.h>
#include<string.h>
#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
	char str[100];//有空格不能用cin ,用str的gets获取数组，转为string 
	gets(str);
	string a=str;
	int l1,l2;
	l1=a.size();
	for(int i=0;i<l1;i++){
		a[i]=tolower(a[i]);
	}
	while(gets(str)){
		string b=str;
		string c=b;
		l2=b.size();
		for(int i=0;i<l2;i++){
			b[i]=tolower(b[i]);
		}
		//在b中删除a
		//先查找位置
		int pos=b.find(a,0);
		while(pos!=-1){
			c.erase(pos,a.size());//原来 
			b.erase(pos,a.size());//位置+长度 
			pos=b.find(a,pos+1);
		}
		pos=b.find(" ",0);
		while(pos!=-1){
			c.erase(pos,1);
			pos=c.find(" ",pos+1);
		} 
		cout<<c <<endl;
	}
	
	
	return 0;		
} 



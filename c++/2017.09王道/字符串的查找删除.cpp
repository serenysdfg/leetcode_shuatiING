#include<stdio.h>
#include<string.h>
#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
	char str[100];//�пո�����cin ,��str��gets��ȡ���飬תΪstring 
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
		//��b��ɾ��a
		//�Ȳ���λ��
		int pos=b.find(a,0);
		while(pos!=-1){
			c.erase(pos,a.size());//ԭ�� 
			b.erase(pos,a.size());//λ��+���� 
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



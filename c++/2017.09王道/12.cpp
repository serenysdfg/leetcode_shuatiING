#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
using namespace std;

map<string ,int>M; //int??
int in[2002];
int main(){
	int n;
	while(scanf("%d",&n)!=EOF&&n!=0){
		for(int i=0;i<2*n;i++){
			in[i]=0;//初始化入度？？干嘛用 
		}
		M.clear();//map映射清空
		int idx=0;//下一个被映射的数字0
		for(int i=0;i<n;i++){
			char str1[50],str2[50];
			scanf("%s%s",str1,str2);
			string a=str1,b=str2;
			int idxa,idxb;
			if(M.find(a)==M.end()){ //没有映射 
				idxa=idx;//??
				M[a]=idx++;//设其映射为idx，并递增idx 
			}
			else idxa=M[a]; //否则，直接读出改映射
		
			if(M.find(b)==M.end()){ //没有映射 
				idxb=idx;//??
				M[b]=idx++;//设其映射为idx，并递增idx 
			}
			else idxb=M[b]; //否则，直接读出改映射
			in[idxb]++;//b的入度递增 	 
		} 
		
		int cnt=0;
		for(int i=0;i<idx;i++){ //统计入度为0的个数 
			if(in[i]==0) cnt++;
		}
		puts(cnt==1?"yes":"no");//只有一个没有入度 
	}
	return 0;
	
	
} 

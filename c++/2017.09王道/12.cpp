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
			in[i]=0;//��ʼ����ȣ��������� 
		}
		M.clear();//mapӳ�����
		int idx=0;//��һ����ӳ�������0
		for(int i=0;i<n;i++){
			char str1[50],str2[50];
			scanf("%s%s",str1,str2);
			string a=str1,b=str2;
			int idxa,idxb;
			if(M.find(a)==M.end()){ //û��ӳ�� 
				idxa=idx;//??
				M[a]=idx++;//����ӳ��Ϊidx��������idx 
			}
			else idxa=M[a]; //����ֱ�Ӷ�����ӳ��
		
			if(M.find(b)==M.end()){ //û��ӳ�� 
				idxb=idx;//??
				M[b]=idx++;//����ӳ��Ϊidx��������idx 
			}
			else idxb=M[b]; //����ֱ�Ӷ�����ӳ��
			in[idxb]++;//b����ȵ��� 	 
		} 
		
		int cnt=0;
		for(int i=0;i<idx;i++){ //ͳ�����Ϊ0�ĸ��� 
			if(in[i]==0) cnt++;
		}
		puts(cnt==1?"yes":"no");//ֻ��һ��û����� 
	}
	return 0;
	
	
} 

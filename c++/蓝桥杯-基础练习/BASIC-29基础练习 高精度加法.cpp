#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int a[401],alen,b[401],blen,c[400],clen;
char st[400];
int main(){
	int i,j,n,len;
	
	scanf("%s",st);//1 
	alen=strlen(st);
	for(i=1;i<=alen;i++){
		a[i]=st[alen-i]-48;   //0是48 s[0]和a[7]是高位 
	}
	scanf("%s",st); //2
	blen=strlen(st);
	for(i=1;i<=blen;i++){
		b[i]=st[blen-i]-48;
	}
	


 	
	if(alen>blen) clen=alen; //clen是大的 
	else clen=blen;
	
	for(i=1;i<=clen;i++)
		 c[i]=a[i]+b[i];
	for(i=1;i<=clen;i++){// 进位 
		if(c[i]>=10){
			c[i+1]=c[i+1]+c[i]/10;
			c[i]=c[i]%10;
		}
	}
	
	
	if(c[clen+1]>0)  clen++;	//输出 
	for(i=clen;i>=1;i--){
		printf("%d",c[i]);
	}
	printf("\n");
	return 0;
	
} 

#include <stdio.h>
#include<cstring> 
void sort(char a[],int len) // 冒泡 ，从大到小 
{
	int i,j,max;
	for(i=0;i<len;i++)
	{
		max=i;
		for(j=i+1;j<len;j++)
			if(a[j]>a[max]) max=j;
		j=a[i];
		a[i]=a[max];
		a[max]=j;
	}
}
void strtoupper(char a[],int len) //字母转换 
{
	int i;
	for(i=0;i<len;i++)
	if(a[i]>='a' && a[i]<='z') a[i]-=32;
}
int mystrcmp(char a[],int l1,char b[],int l2)
{
	if(l1!=l2) return 0;
	int i;
	for(i=0;i<l1;i++)
	if(a[i]!=b[i]) return 0;
	return 1;
}

/*
int mystrlen(char *p)
{
	int l=0;
	while(*p++!=0)
	l++;
	return l;
}*/
int main()
{
	char s1[1000]={0},s2[1000]={0};  //初始化 
	int l1,l2;
	scanf("%s%s",s1,s2);
	l1=strlen(s1);
	l2=strlen(s2);
	
	strtoupper(s1,l1);
	strtoupper(s2,l2);
	
	sort(s1,l1);
	sort(s2,l2);
    if(mystrcmp(s1,l1,s2,l2)) printf("Y");
    else printf("N");
return 0;
}


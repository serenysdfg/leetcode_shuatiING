#include<iostream>
using namespace std;
int main(){
	char c;
	int a,b;
	cin>>c>>a>>b;
	int res;
	if(c=='+')res=a+b;
	else if(c=='-')res=a-b;
	else if(c=='*')res=a*b;
	else res=a/b;
	cout<<res;
	return 0;
}


/*
cÓïÑÔ
#include<stdio.h>
int main()
{ int a[2];
  int i,j;
  char c=getchar();
  for(i=0;i<2;i++)
  scanf("%d",&a[i]);
  if(c=='+')
	  j=a[0]+a[1];
  else if(c=='-')
	  j=a[0]-a[1];
  else if(c=='*')
	  j=a[0]*a[1];
  else if(c=='/')
	  j=a[0]/a[1];
  printf("%d",j);
  return 0;
}

*/ 

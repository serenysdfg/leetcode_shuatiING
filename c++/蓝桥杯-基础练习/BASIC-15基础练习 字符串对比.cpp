/*
��1�������ַ������Ȳ��ȡ����� Beijing �� Hebei
����2�������ַ�������������ȣ�������Ӧλ���ϵ��ַ���ȫһ��(���ִ�Сд)������ Beijing �� Beijing
����3�������ַ���������ȣ���Ӧλ���ϵ��ַ����ڲ����ִ�Сд��ǰ���²��ܴﵽ��ȫһ�£�Ҳ����˵���������������2�������� beijing �� BEIjing
����4�������ַ���������ȣ����Ǽ�ʹ�ǲ����ִ�СдҲ����ʹ�������ַ���һ�¡����� Beijing �� Nanjing
��������ж�����������ַ���֮��Ĺ�ϵ�����������е���һ�࣬������������ı�š�
*/

#include<stdio.h>
#include<string.h>
int main()
{
	char a[10],b[10],i,n,l=2;//�ȼ���l=2 
	gets(a);gets(b); //gets,strlen ��a[i] 
	n=strlen(a);
	if(strlen(b)!=n)l=1;
	else
	{
	for(i=0;i<n;i++)
		if(a[i]==b[i]||a[i]==b[i]+32||a[i]+32==b[i])  //��A65 
			if(a[i]!=b[i])l=3;
			else ;
		else {l=4;break;}
	}
printf("%d",l);
return 0;
}  

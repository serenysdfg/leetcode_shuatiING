/*
　1：两个字符串长度不等。比如 Beijing 和 Hebei
　　2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing
　　3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和 BEIjing
　　4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing
　　编程判断输入的两个字符串之间的关系属于这四类中的哪一类，给出所属的类的编号。
*/

#include<stdio.h>
#include<string.h>
int main()
{
	char a[10],b[10],i,n,l=2;//先假设l=2 
	gets(a);gets(b); //gets,strlen 。a[i] 
	n=strlen(a);
	if(strlen(b)!=n)l=1;
	else
	{
	for(i=0;i<n;i++)
		if(a[i]==b[i]||a[i]==b[i]+32||a[i]+32==b[i])  //大A65 
			if(a[i]!=b[i])l=3;
			else ;
		else {l=4;break;}
	}
printf("%d",l);
return 0;
}  

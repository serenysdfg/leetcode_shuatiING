#include<stdio.h>
#include<string.h>
//字符串的分割
int splite(char *s1,char *s2,int pos){
	int i,j;
	i=pos;
	while(s1[i]==' ' )i++;
	if(s1[i]!='\0'){
		j=0;
		//复制非空格符直到找到下一个空格符
		while(s1[i]!='\0'&&s1[i]!=' '){
			s2[j]=s1[i];
			i++;
			j++;
		} 
		s2[j]='\0';
		return i;
	}
	else
		return -1;
} 




int main(){
	char string[50];
	char partition_string[20];
	int position;
	int k;
	printf("\nPlease input string:");
	gets(string);
	position=0;
	printf("\nPartition result:\n");
	//进行字符串分割，知道字符创结束 
	k=0;
	while((position=splite(string,partition_string,position))!=-1){
		k++;
		//输出各分割出来的子字符串
		printf("Partition %d: %s\n",k,partition_string); 
	}
	return 0;
}

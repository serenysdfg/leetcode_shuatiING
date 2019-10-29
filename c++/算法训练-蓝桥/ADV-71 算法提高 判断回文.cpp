#include<stdio.h>
#include<string.h>
bool check(char *a){
	int len=strlen(a);
	int i,j;
	for(i=0, j=len-1;i<=j;i++,j--){
		if(a[i]!=a[j])
			return false;
	}
	return true;
}
int main(){
	char a[200];
	scanf("%s",a);
	if(check(a)==true)
		printf("yes!\n");
	else
		printf("no!\n");
	return 0;
} 

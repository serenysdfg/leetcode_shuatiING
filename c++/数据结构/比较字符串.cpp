#include <stdio.h>
#include <string.h>
#include <iostream>
#include<functional>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
const int maxn = 135;
int n;
char str1[maxn],str2[maxn];
int main()
{
	#ifndef ONLINE_JUDGE  
	freopen("data.txt","r",stdin);  
	#endif 	
	scanf("%s%s",&str1,&str2);
	int len1 = strlen(str1);
	int len2 = strlen(str2);
	int len = len1<len2?len1:len2;
	if( len1 == len2 ){
		puts("0");
	}
	else
		for( int i = 0; i <= len; i ++ ){
			if( str1[i] != str2[i] ){
				printf("%d\n",str1[i]-str2[i]);
				break;
			}
		}
	return 0;
}


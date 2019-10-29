#include<cstdio> 
#include<iostream> 
using namespace std; 

int changes(char s[],char x,int n) 
{ 
   int i,change=0,j,k; 
   for(i=0;i<n/2;i++) 
   { 
      if(s[i]==x)  //移到中间 
      { 
         for(j=i;j<n-i-1;j++)  //对称，i+j=n-1 
            if(s[n-i-1]==s[j]) //从左侧该位置开始，找相同字母
                break; 

         change+=j-i; //需要j-i次移动可到左侧位置

         for(k=j;k>i;k--) //实现字母的移动 
            s[k]=s[k-1]; 

         s[i]=s[n-i-1]; 
      } 
      else 
      { 
         for(j=n-i-1;j>=i;j--) 
            if(s[i]==s[j]) 
               break; 
         change+=n-i-1-j; 

         for(k=j;k<n-i-1;k++)  s[k]=s[k+1]; 
         s[n-i-1]=s[i]; 
      } 
    } 
    return change; 
} 
int main(){
	int n,i,k=0,b[26]={0},j;  //b[26]={0} 
	char y,s[8001]={0};
	scanf("%d\n",&n);
	for(i=0;i<n;i++){  //b【n】字母个数，s【i】 读字符串char s【】，x单数，n个数 
		scanf("%c",&s[i]);
		b[s[i]-'a']++;
	}
	char x;
	for(j=0;j<26;j++){
		if(b[j]%2!=0){
			k++;
			x=j+'a'; //x是单数字母个数 
		}
	}
	if(k>=2)
	 	printf("Impossible\n"); //不可能 ，单数字母个数>=2 
	else 
    { 
       printf("%d\n",changes(s,x,n)); //输出最少的交换次数。 
       return 0; 
    } 
}


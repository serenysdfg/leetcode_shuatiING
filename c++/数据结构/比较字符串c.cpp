#include<stdio.h>
#include<string.h>
int min(int a,int b)
{
return a>b?b:a;
}
int main()
{
char a[1000];
char b[1000];
scanf("%s",a);
scanf("%s",b);
int k=min(strlen(a),strlen(b)),i1;
int ok=1;
for(i1=0;i1<k;i1++)
{       if(a[i1]!=b[i1])
        {   printf("%d\n",a[i1]-b[i1]);
            ok=0;
             break;
         }
}
if(ok==1)
if(strlen(a)==strlen(b))
    printf("0\n");
else if(strlen(a)>strlen(b))
     printf("%d\n",a[i1]);
 else 
    printf("%d\n",b[i1]);
return 0;  
}


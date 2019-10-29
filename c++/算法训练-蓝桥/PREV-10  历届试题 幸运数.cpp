    #include"stdio.h"  
    #include"stdlib.h"  
    #include"time.h"  
    #define max 1000000  
    int main()  
    {//long long int a[max];//建立一张幸运数的表,因为数组过大,采用指针方式开辟空间  
    long int i,j=0;  
    long int temp=max,kk=1;  
    long int temp1=0;  
    long int *a;  
    long int m,n;  
    long start,finish;  
    a=(long int *)malloc(sizeof(long int)*max);  
    for(i=0;i<max;i++)  
    a[i]=i+1;//赋予初值  
    scanf("%ld %ld",&m,&n);  
    start=clock();//开始时间  
      
    for(i=0;i<temp;)//a[k]为每一次保存的模  
    { if(a[i]>kk) { kk=a[i];}  
    else   
    {i++;  
        continue;}  
      //根据每一次保存的模将上一次中"相关"的数字给排除掉    
    temp1=0;  
    for(j=kk;j<temp;j+=kk)  
      {a[j-1]=0;  
       temp1++;;//每将一个数字变为0后,temp++  
       }  
    long int temp2=0;  
    for(j=0;j<temp;j++)  
    {if(a[j]) a[temp2++]=a[j];  
    }//重新排列,将有零的"去掉"  
    temp-=temp1;//剩下数字的总数减少  
    }//end for i  
      
    for(i=0;i<temp;i++)  
    if(a[i]&&a[i]>m&&a[i]<n)  
    printf("%ld ",a[i]);  
    printf("\n");  
    finish=clock();//结束时间  
      
    printf("\nall time: %lfs",(finish-start)/1000.0);  
    system("pause"); }  

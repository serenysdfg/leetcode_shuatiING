    #include"stdio.h"  
    #include"stdlib.h"  
    #include"time.h"  
    #define max 1000000  
    int main()  
    {//long long int a[max];//����һ���������ı�,��Ϊ�������,����ָ�뷽ʽ���ٿռ�  
    long int i,j=0;  
    long int temp=max,kk=1;  
    long int temp1=0;  
    long int *a;  
    long int m,n;  
    long start,finish;  
    a=(long int *)malloc(sizeof(long int)*max);  
    for(i=0;i<max;i++)  
    a[i]=i+1;//�����ֵ  
    scanf("%ld %ld",&m,&n);  
    start=clock();//��ʼʱ��  
      
    for(i=0;i<temp;)//a[k]Ϊÿһ�α����ģ  
    { if(a[i]>kk) { kk=a[i];}  
    else   
    {i++;  
        continue;}  
      //����ÿһ�α����ģ����һ����"���"�����ָ��ų���    
    temp1=0;  
    for(j=kk;j<temp;j+=kk)  
      {a[j-1]=0;  
       temp1++;;//ÿ��һ�����ֱ�Ϊ0��,temp++  
       }  
    long int temp2=0;  
    for(j=0;j<temp;j++)  
    {if(a[j]) a[temp2++]=a[j];  
    }//��������,�������"ȥ��"  
    temp-=temp1;//ʣ�����ֵ���������  
    }//end for i  
      
    for(i=0;i<temp;i++)  
    if(a[i]&&a[i]>m&&a[i]<n)  
    printf("%ld ",a[i]);  
    printf("\n");  
    finish=clock();//����ʱ��  
      
    printf("\nall time: %lfs",(finish-start)/1000.0);  
    system("pause"); }  

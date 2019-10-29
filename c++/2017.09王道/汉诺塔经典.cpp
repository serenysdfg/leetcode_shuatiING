    #include<stdio.h>  
      
    void hanota(int num,char A,char B,char C)  
    {  
     //如果只有一个元素，那么直接把这个元素，移动到C  
     if(1==num)  
     {  
         printf("把第%d个元素从%c移动到%c\n",num,A,C);  
     }else{  
     //如果不是第一个元素，先把前n-1个元素，借助C移动到B  
       hanota(num-1,A,C,B);  
     //然后把A最下面的元素移动到C  
       printf("把第%d个元素从%c移动到%c\n",num,A,C);  
       //然后再把B上的元素借助A移动到C  
       hanota(num-1,B,A,C);  
     }  
    }  
    int main()  
    {  
        char A='A';  
        char B='B';  
        char C='C';  
        hanota(3,A,B,C);  
        return 0;  
    }  

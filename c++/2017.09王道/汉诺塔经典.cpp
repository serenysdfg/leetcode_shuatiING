    #include<stdio.h>  
      
    void hanota(int num,char A,char B,char C)  
    {  
     //���ֻ��һ��Ԫ�أ���ôֱ�Ӱ����Ԫ�أ��ƶ���C  
     if(1==num)  
     {  
         printf("�ѵ�%d��Ԫ�ش�%c�ƶ���%c\n",num,A,C);  
     }else{  
     //������ǵ�һ��Ԫ�أ��Ȱ�ǰn-1��Ԫ�أ�����C�ƶ���B  
       hanota(num-1,A,C,B);  
     //Ȼ���A�������Ԫ���ƶ���C  
       printf("�ѵ�%d��Ԫ�ش�%c�ƶ���%c\n",num,A,C);  
       //Ȼ���ٰ�B�ϵ�Ԫ�ؽ���A�ƶ���C  
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

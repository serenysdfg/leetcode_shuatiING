    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    struct Arr{  
    int len;//�����ܴ�ȡ�����Ԫ�ظ���  
    int cnu;//�����е�ǰԪ�ظ���  
    int * pBase;//�洢ָ�������ָ��  
    };  
      
      
    /** 
    *��ʼ������ 
    */  
    void init_array(struct Arr * pArray,int len){  
    pArray->pBase=(int *)malloc(sizeof(int)*len);//����4*len�ֽڳ��ȵ��ڴ�  
    if(NULL== pArray->pBase)//�ж��ڴ��Ƿ����ʧ��  
    {  
        printf("��̬�����ڴ�ʧ��\n");  
       // exit(-1);  
    }else{  
    pArray->len=len;  
    pArray->cnu=0;  
    }  
    return ;  
    }  
      
    /** 
    *�ж������Ƿ�Ϊ�գ�����ַʡ�ڴ�4�ֽڣ����ṹ�������Ҫ���п�����12�ֽ� 
    */  
    bool isempty(struct Arr * pArray){  
    if(0==pArray->cnu)  
    {  
        return true;  
    }else{  
    return false;  
    }  
    }  
      
    /** 
    **�ж������Ƿ����� 
    */  
    bool isfull(struct Arr * pArray)  
    {  
      if(pArray->len==pArray->cnu)  
      {  
      
          return true;  
      }else {  
      return false;  
      }  
      
    }  
    /** 
    *��ʾ�������� 
    */  
    void show_array(struct Arr * pArray){  
    if(isempty(pArray))  
        printf("����Ϊ�գ�\n");  
    else{  
        int i;  
        for( i=0; i<pArray->cnu;i++)  
        {  
            printf("%d \n",pArray->pBase[i]);  
        }  
        printf("------------------------------------\n");  
    }  
    }  
      
    /** 
    **������׷��Ԫ�� 
    */  
    bool append(struct Arr * pArray,int val){  
    if(isfull(pArray))  
    {  
     printf("�����Ѿ����ˣ�\n");  
     return false;  
    }else{  
        pArray->pBase[pArray->cnu]=val;  
        pArray->cnu++;  
      
    }  
    }  
      
      
    /** 
    **�������в���Ԫ��,posΪ�����еڼ���λ�ã�pos=3������a[2]����Ԫ�� 
    */  
      
    bool insert(struct Arr * pArray,int pos,int val)  
    {  
       if(pos<1||pos>pArray->len+1)//�����λ�ò���С��1��ͬʱ���ܱ����һ��Ԫ�ش��  
       {  
       printf("�����λ������Ĳ��Ϸ�\n");  
       return false;  
       }  
       if(isfull(pArray))  
       {  
           printf("�����Ѿ�����,����ʧ�ܣ�\n");  
          return false;  
        }  
        int i;  
        //ѭ����posλ�ÿ�ʼ���������  
       for(i=pArray->cnu;i>=pos;i--)  
        //�ƶ���Χ�Ǵӵ�pos������cnu��  
       {  
           pArray->pBase[i]=pArray->pBase[i-1];  
           /** 
           ����i��ʾҪ�ƶ�Ԫ�ص�λ�ã���һ��ʼ�ġ��ұ߶���i-1,�����ƣ������i-2,���ƣ������i 
           */  
       }  
      
      
      
           pArray->pBase[pos-1]=val;  
           pArray->cnu++;  
           pArray->len++;  
           return true;  
    }  
    /** 
    **ɾ�������еĵ�pos��Ԫ�أ�ͬʱ����ɾ����Ԫ�ص�ֵ 
    */  
      
    bool delete(struct Arr * pArray,int pos,int * val)  
    {  
         if(pos<1||pos>pArray->cnu)  
         {  
             printf("ɾ��ʧ�ܣ�λ�ò��Ϸ�\n");  
             return false;  
         }  
         int i;  
         *val=pArray->pBase[pos-1];  
         for(i=pos+1;i<=pArray->cnu;i++)  
         {  
             //�ƶ���λ�Ǵӵ�pos+1����cnu  
             pArray->pBase[i-2]=pArray->pBase[i-1];  
      
         }  
          pArray->cnu--;  
          return true;  
      
    }  
      
    /** 
    **���鵹�� 
    */  
      
    bool inverse(struct Arr * pArray)  
    {  
    if(isempty(pArray))  
    {  
        printf("����ʧ�ܣ�������Ϊ��");  
        return false;  
    }  
      
    int i=0;  
    int j=pArray->cnu-1;  
      
        int temp;  
    while(i<j)  
    {  
        temp=pArray->pBase[i];  
        pArray->pBase[i]= pArray->pBase[j];  
         pArray->pBase[j]=temp;  
         i++;  
         j--;  
    }  
    return true;  
      
    }  
    int main()  
    {  
        struct Arr arr;  
        init_array(&arr,6);//���ṹ��ĵ�ַ��Ϊʵ�Σ����������޸Ľṹ���е�ֵ����������ǽṹ���������ô�����п���������ı�ֵ  
        append(&arr,1);  
        append(&arr,2);  
        append(&arr,3);  
        append(&arr,4);  
        show_array(&arr);  
        insert(&arr,2,88);  
         show_array(&arr);  
         int val;  
         delete(&arr,1,&val);  
         show_array(&arr);  
         printf("ɾ���� %d\n",val);  
         inverse(&arr);  
        show_array(&arr);  
        return 0;  
    }  

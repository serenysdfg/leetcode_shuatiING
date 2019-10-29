    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    struct Arr{  
    int len;//数组能存取的最大元素个数  
    int cnu;//数组中当前元素个数  
    int * pBase;//存储指向数组的指针  
    };  
      
      
    /** 
    *初始化数组 
    */  
    void init_array(struct Arr * pArray,int len){  
    pArray->pBase=(int *)malloc(sizeof(int)*len);//分配4*len字节长度的内存  
    if(NULL== pArray->pBase)//判断内存是否分配失败  
    {  
        printf("动态分配内存失败\n");  
       // exit(-1);  
    }else{  
    pArray->len=len;  
    pArray->cnu=0;  
    }  
    return ;  
    }  
      
    /** 
    *判断数组是否为空，传地址省内存4字节，传结构体变量需要进行拷贝，12字节 
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
    **判断数组是否满了 
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
    *显示数组内容 
    */  
    void show_array(struct Arr * pArray){  
    if(isempty(pArray))  
        printf("数组为空！\n");  
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
    **向数组追加元素 
    */  
    bool append(struct Arr * pArray,int val){  
    if(isfull(pArray))  
    {  
     printf("数组已经满了！\n");  
     return false;  
    }else{  
        pArray->pBase[pArray->cnu]=val;  
        pArray->cnu++;  
      
    }  
    }  
      
      
    /** 
    **向数组中插入元素,pos为数组中第几个位置，pos=3就是向a[2]插入元素 
    */  
      
    bool insert(struct Arr * pArray,int pos,int val)  
    {  
       if(pos<1||pos>pArray->len+1)//插入的位置不能小于1，同时不能比最后一个元素大二  
       {  
       printf("插入的位置输入的不合法\n");  
       return false;  
       }  
       if(isfull(pArray))  
       {  
           printf("数组已经满了,插入失败！\n");  
          return false;  
        }  
        int i;  
        //循环将pos位置开始的数组后移  
       for(i=pArray->cnu;i>=pos;i--)  
        //移动范围是从第pos个到底cnu个  
       {  
           pArray->pBase[i]=pArray->pBase[i-1];  
           /** 
           若以i表示要移动元素的位置，从一开始的。右边都是i-1,若左移，左边是i-2,右移，左边是i 
           */  
       }  
      
      
      
           pArray->pBase[pos-1]=val;  
           pArray->cnu++;  
           pArray->len++;  
           return true;  
    }  
    /** 
    **删除数组中的第pos个元素，同时返回删除的元素的值 
    */  
      
    bool delete(struct Arr * pArray,int pos,int * val)  
    {  
         if(pos<1||pos>pArray->cnu)  
         {  
             printf("删除失败，位置不合法\n");  
             return false;  
         }  
         int i;  
         *val=pArray->pBase[pos-1];  
         for(i=pos+1;i<=pArray->cnu;i++)  
         {  
             //移动单位是从第pos+1个到cnu  
             pArray->pBase[i-2]=pArray->pBase[i-1];  
      
         }  
          pArray->cnu--;  
          return true;  
      
    }  
      
    /** 
    **数组倒置 
    */  
      
    bool inverse(struct Arr * pArray)  
    {  
    if(isempty(pArray))  
    {  
        printf("倒置失败，因数组为空");  
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
        init_array(&arr,6);//将结构体的地址作为实参，这样才能修改结构体中的值，如果传的是结构体变量，那么将进行拷贝，不会改变值  
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
         printf("删除了 %d\n",val);  
         inverse(&arr);  
        show_array(&arr);  
        return 0;  
    }  

    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    //ջ��һ���������Ч���ݵ�ͷ�ڵ㣬Pbotomʼ��ָ��ͷ��㡣  
    /** 
    **����ڵ�Ľṹ�� 
    */  
     typedef struct Node{  
       int data;//������  
       struct Node * PNext;//ָ����  
    } Node,*PNext;  
    /** 
    **����ջ�Ľṹ�� 
    */  
    typedef struct Stack {  
     PNext top;  
    PNext bottom;  
    }Stack,* PStack;  
    /** 
    **��ʼ��ջ 
    */  
    void  init(PStack PStack )  
    {  
        //����һ�������κ�����Ԫ�ص�ͷ��㣬��Ϊջ��  
       PStack->bottom=malloc(sizeof(Node));  
       PStack->top=PStack->bottom;  
       PStack->top->PNext=NULL;  
    }  
    /** 
    *����ջ 
    **/  
    void traverse(PStack Ps )  
    {  
        if(Ps->bottom==Ps->top)  
        {  
            printf("ջΪ��\n");  
            return ;  
        }  
        PNext pt=Ps->top;  
        while(pt!=Ps->bottom)//���ܰ�pt����ps->top�������޸����������Ρ���  
        {  
           printf("%d ",pt->data);  
           pt=pt ->PNext;  
        }  
        printf("\n");  
        return ;  
      
    }  
    /** 
    **��ջ 
    */  
    void push(PStack Pstack,int val)  
    {  
       PNext Pnew=malloc(sizeof(Node));//����һ���½ڵ�  
       Pnew->data=val;  
       Pnew->PNext=Pstack->top;  
       Pstack->top=Pnew;  
    }  
    /** 
    **��ջ 
    */  
    void pop(PStack ps )  
    {  
      if(ps->top==ps->bottom)  
      {  
          printf("ջΪ�գ��޷���ɳ�ջ����\n");  
          return;  
      }  
      PNext temp=ps->top;//���븨�������������ͷ��ڴ�  
      ps->top=ps->top->PNext;  
      free(temp);  
      temp=NULL;  
    }  
            free(temp);  
        }  m       
    }  
    int main()  
    {  
    Stack stack;  
    init(&stack);  
    push(&stack,6);  
    push(&stack,7);  
    push(&stack,8);  
    traverse(&stack);  
    pop(&stack);  
    traverse(&stack);  
    clear(&stack);  
    traverse(&stack);  
    push(&stack,7);  
    traverse(&stack);  
    return 0;  
    }  

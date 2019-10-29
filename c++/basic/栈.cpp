    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    //栈有一个不存放有效数据的头节点，Pbotom始终指向头结点。  
    /** 
    **定义节点的结构体 
    */  
     typedef struct Node{  
       int data;//数据域  
       struct Node * PNext;//指针域  
    } Node,*PNext;  
    /** 
    **定义栈的结构体 
    */  
    typedef struct Stack {  
     PNext top;  
    PNext bottom;  
    }Stack,* PStack;  
    /** 
    **初始化栈 
    */  
    void  init(PStack PStack )  
    {  
        //建立一个不存任何有限元素的头结点，作为栈底  
       PStack->bottom=malloc(sizeof(Node));  
       PStack->top=PStack->bottom;  
       PStack->top->PNext=NULL;  
    }  
    /** 
    *遍历栈 
    **/  
    void traverse(PStack Ps )  
    {  
        if(Ps->bottom==Ps->top)  
        {  
            printf("栈为空\n");  
            return ;  
        }  
        PNext pt=Ps->top;  
        while(pt!=Ps->bottom)//不能把pt换成ps->top这样就修改了链表。尴尬。。  
        {  
           printf("%d ",pt->data);  
           pt=pt ->PNext;  
        }  
        printf("\n");  
        return ;  
      
    }  
    /** 
    **入栈 
    */  
    void push(PStack Pstack,int val)  
    {  
       PNext Pnew=malloc(sizeof(Node));//生成一个新节点  
       Pnew->data=val;  
       Pnew->PNext=Pstack->top;  
       Pstack->top=Pnew;  
    }  
    /** 
    **出栈 
    */  
    void pop(PStack ps )  
    {  
      if(ps->top==ps->bottom)  
      {  
          printf("栈为空，无法完成出栈操作\n");  
          return;  
      }  
      PNext temp=ps->top;//引入辅助变量，用于释放内存  
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

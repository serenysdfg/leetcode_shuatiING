    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    typedef struct Queue{  
    int * PBase;//指向数组第一个元素的指针  
    int front;//队列头部元素下标  
    int rear;//队列尾部元素下标  
    }QUEUE;  
    /** 
    *初始化队列，实现队列的数组长度为6。 
    **/  
    void initQueue(QUEUE * pQ)  
    {  
        pQ->PBase=malloc(sizeof(int)*6);  
        pQ->front=0;  
        pQ->rear=0;  
    }  
    /** 
    判断队列是否已满 
    */  
    bool isFull(QUEUE * pQ)  
    {  
    if((pQ->rear+1)%6==pQ->front)  
    {  
        printf("队列已满，无法插入");  
        return true;  
    }  
      
    return false;  
    }  
      
    /** 
    判断队列是否为空 
    */  
      
      
    bool isEmpty(QUEUE * pQ)  
    {  
      if(pQ->front==pQ->rear)  
      {  
          printf("队列为空");  
          return true;  
      }  
    return false;  
      }  
    /** 
    入队 
    */  
    bool insert(QUEUE * pQ,int val)  
    {  
      if(isFull(pQ))  
        return false;  
      pQ->PBase[pQ->rear]=val;  
      pQ->rear=(pQ->rear+1)%6;  
      return true;  
    }  
      
    /** 
    遍历队列 
    */  
      
    void traverse(QUEUE * pQ)  
    {  
        int i=pQ->front;  
        while(i!=pQ->rear)  
        {  
            printf("%d  ",pQ->PBase[i]);  
            i++;  
        }  
        printf("\n");  
    }  
      
    /** 
    出队 
    */  
      
    bool  out_queue(QUEUE * pQ)  
    {  
      if(isEmpty(pQ))  
        return false;  
      
      pQ->front=(pQ->front+1)%6;  
      
    }  
      
      
      
    int main()  
    {  
      
    QUEUE Q;  
    initQueue(&Q);  
    insert(&Q,1);  
    insert(&Q,2);  
    insert(&Q,3);  
    insert(&Q,4);  
    insert(&Q,5);  
    insert(&Q,6);  
    traverse(&Q);  
    out_queue(&Q);  
    traverse(&Q);  
    return 0;  
    }  

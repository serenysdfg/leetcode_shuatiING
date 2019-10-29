    #include<stdio.h>  
    #include<malloc.h>  
    #include<stdbool.h>  
    typedef struct Queue{  
    int * PBase;//ָ�������һ��Ԫ�ص�ָ��  
    int front;//����ͷ��Ԫ���±�  
    int rear;//����β��Ԫ���±�  
    }QUEUE;  
    /** 
    *��ʼ�����У�ʵ�ֶ��е����鳤��Ϊ6�� 
    **/  
    void initQueue(QUEUE * pQ)  
    {  
        pQ->PBase=malloc(sizeof(int)*6);  
        pQ->front=0;  
        pQ->rear=0;  
    }  
    /** 
    �ж϶����Ƿ����� 
    */  
    bool isFull(QUEUE * pQ)  
    {  
    if((pQ->rear+1)%6==pQ->front)  
    {  
        printf("�����������޷�����");  
        return true;  
    }  
      
    return false;  
    }  
      
    /** 
    �ж϶����Ƿ�Ϊ�� 
    */  
      
      
    bool isEmpty(QUEUE * pQ)  
    {  
      if(pQ->front==pQ->rear)  
      {  
          printf("����Ϊ��");  
          return true;  
      }  
    return false;  
      }  
    /** 
    ��� 
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
    �������� 
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
    ���� 
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

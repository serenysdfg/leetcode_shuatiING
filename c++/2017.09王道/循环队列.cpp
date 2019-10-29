#include <stdio.h> 
  #include <stdlib.h> 
  #include <string.h> 
    
  #define queuesize 100001  //最大队列长度 
    
  struct queue 
  { 
    int front; 
    int rear; 
    int data[queuesize]; 
    int count; //记录队列中的元素 
  }; 
    
  void InitQueue(struct queue *Q); 
  void EnQueue(struct queue *Q, int element, int m); 
  void Dequeue(struct queue *Q, int m); 
  void QueueSearch(struct queue *Q, int k, int m); 
    
  int main() 
  { 
    int n, m, i, element, k, flag; 
    char command[10]; 
  
    
    while(scanf("%d%d",&n, &m) != EOF) 
    { 
      if(n < 1 || m > 100000) 
        return 0; 
      struct queue *Q; 
      Q = malloc(sizeof(struct queue)); 
      InitQueue(Q); 
      for(i = 0; i < n; i ++) 
      { 
        scanf("%s",command); 
        if (strcmp(command,"Push") == 0) 
        { 
          scanf("%d",&element); 
          EnQueue(Q, element, m); 
        }else if (strcmp(command,"Pop") == 0) 
        { 
          Dequeue(Q, m); 
        }else if (strcmp(command,"Query") == 0) 
        { 
          scanf("%d",&k); 
          QueueSearch(Q, k, m); 
        }else if (strcmp(command,"Isempty") == 0) 
        { 
          flag = (Q -> count == 0)? 1 : 0; 
          if(flag) 
          { 
            printf("yes\n"); 
          }else
          { 
            printf("no\n"); 
          } 
        }else if (strcmp(command,"Isfull") == 0) 
        { 
          flag = (Q -> count == m)? 1 : 0; 
          if(flag) 
          { 
            printf("yes\n"); 
          }else
          { 
            printf("no\n"); 
          } 
        } 
      } 
    }   
    return 0; 
  } 
    
  /** 
   * Description:队列初始化 
   */
  void InitQueue(struct queue *Q) 
  { 
    Q -> front = Q -> rear = 0; 
    Q -> count = 0; 
  } 
    
  /** 
   * Description:入队操作 
   */
  void EnQueue(struct queue *Q, int element, int m) 
  { 
    int flag; 
    flag = (Q -> count == m)? 1 : 0;  
    
    if(!flag) 
    { 
      Q -> data[Q -> rear] = element; 
      Q -> count ++; 
      Q -> rear = (Q -> rear + 1) % m; 
    }else
    { 
      printf("failed\n"); 
    } 
  } 
    
  /** 
   * Description:出队操作 
   */
  void Dequeue(struct queue *Q, int m) 
  { 
    int flag; 
    int element; 
    
    flag = (Q -> count == 0)? 1 : 0; 
    
    if(!flag) 
    { 
      element = Q -> data[Q -> front]; 
      Q -> front = (Q -> front + 1) % m; 
      Q -> count --; 
    }else
    { 
      printf("failed\n"); 
    } 
  } 
    
  /** 
   * Description:查找队列中的指定元素 
   */
  void QueueSearch(struct queue *Q, int k, int m) 
  { 
    int flag, temp; 
    flag = (Q -> count == 0)? 1: 0; 
    temp = Q -> front + k - 1; 
    if((!flag) && (k <= m && k >= 1)) 
    { 
      if((Q -> front < Q -> rear) && ( Q-> front <= temp && Q -> rear > temp)) 
        printf("%d\n",Q -> data[temp]); 
      else if((Q -> front > Q -> rear) && (temp >= Q -> front || temp < Q->rear)) 
        printf("%d\n",Q -> data[temp]); 
      else if(Q -> front == Q -> rear) 
        printf("%d\n",Q -> data[temp]); 
      else
        printf("failed\n"); 
    }else
    { 
      printf("failed\n"); 
    } } 

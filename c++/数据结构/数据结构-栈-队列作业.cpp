#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define SUCCESS 1
#define FAILURE 0
#define MAXSIZE 100 //队列最大容量

typedef struct node{
	int no;
	char *text;
	struct node *next;
}Task; 

typedef struct{
	Task *front;
	Task *rear;
}LinkQueue;

//初始化一个空的链式队列
int InitQueue(LinkQueue *Q){
	Q->front=(Task*) malloc(sizeof(Task));
	if(Q->front!=NULL){
		Q->rear=Q->front;  //相同 
		Q->front->next=NULL;  //null 
		return SUCCESS;
	}
	else
		return FAILURE; //内存分配失败 
} 


OutputPrintTask(LinkedQueue Q){
	Task *p;
	printf("\n当前队列\n");
	printf("作业号，文本");
	for(p=Q.front->next;p;p=p->next){
		/*输出队列中打印的作业的标识号和内容*/
		printf("\n %d,%s",p->no,p->text); 
	}
	
} 

//入队操作，加到队尾
void EnPrintTaskQueue(LinkedQueue *Q,int no,char *text){
	Task *p;
	p=(Task*) malloc(sizeof(Task));
	p->text=(char)malloc(strlen(text)*sizeof(char)+1);
	//开辟空间存放打印的内容
	strcpy(p->text,text);
	p->no=no;
	p->next=NULL;
	//新节点入队，修改队尾指针
	Q->rear->next=p;
	Q->rear=p; 
} 
//出队操作
int DePrintTaskQueue(LinkQueue *Q){
	Task *p;
	if(Q->front==Q->rear)
		return FAILURE;
	p=Q->front->next;
	if(Q->rear==p)
		Q->rear=Q->front;
	Q->front->next=p->next;
	printf("当前打印任务序号：%d\n",p->no);
	printf("当前打印内容：%s\n",p->next);
	free(p);
	return SUCCESS;
		
} 


//主程序
int main(){
	LinkQueue Q;int m,no; char str[MAXSIZE];
	InitQueue(&Q);
	while(1){
		printf("\n***添加打印任务：1***\n "); //打印菜单 
		printf("***执行打印任务：2***\n");
		printf("***结束：0***\n");
		printf("请选择任务：");
		scanf("%d",&m);
		if(m=0)
			break;
		if(m==1){
			printf("请输入，编号和文本内容（使用，间隔，文本长度小于100）\n");
			scanf("%d,%s",&no,str);
			EnPrintTaskQueue(&Q,no,str);
			OutputPrintTask(Q);
		} 
		else{
			//作业出队
			DePrintTaskQueue(&Q); 
		}
	}
} 

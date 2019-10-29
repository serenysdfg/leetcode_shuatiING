#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define SUCCESS 1
#define FAILURE 0
#define MAXSIZE 100 //�����������

typedef struct node{
	int no;
	char *text;
	struct node *next;
}Task; 

typedef struct{
	Task *front;
	Task *rear;
}LinkQueue;

//��ʼ��һ���յ���ʽ����
int InitQueue(LinkQueue *Q){
	Q->front=(Task*) malloc(sizeof(Task));
	if(Q->front!=NULL){
		Q->rear=Q->front;  //��ͬ 
		Q->front->next=NULL;  //null 
		return SUCCESS;
	}
	else
		return FAILURE; //�ڴ����ʧ�� 
} 


OutputPrintTask(LinkedQueue Q){
	Task *p;
	printf("\n��ǰ����\n");
	printf("��ҵ�ţ��ı�");
	for(p=Q.front->next;p;p=p->next){
		/*��������д�ӡ����ҵ�ı�ʶ�ź�����*/
		printf("\n %d,%s",p->no,p->text); 
	}
	
} 

//��Ӳ������ӵ���β
void EnPrintTaskQueue(LinkedQueue *Q,int no,char *text){
	Task *p;
	p=(Task*) malloc(sizeof(Task));
	p->text=(char)malloc(strlen(text)*sizeof(char)+1);
	//���ٿռ��Ŵ�ӡ������
	strcpy(p->text,text);
	p->no=no;
	p->next=NULL;
	//�½ڵ���ӣ��޸Ķ�βָ��
	Q->rear->next=p;
	Q->rear=p; 
} 
//���Ӳ���
int DePrintTaskQueue(LinkQueue *Q){
	Task *p;
	if(Q->front==Q->rear)
		return FAILURE;
	p=Q->front->next;
	if(Q->rear==p)
		Q->rear=Q->front;
	Q->front->next=p->next;
	printf("��ǰ��ӡ������ţ�%d\n",p->no);
	printf("��ǰ��ӡ���ݣ�%s\n",p->next);
	free(p);
	return SUCCESS;
		
} 


//������
int main(){
	LinkQueue Q;int m,no; char str[MAXSIZE];
	InitQueue(&Q);
	while(1){
		printf("\n***��Ӵ�ӡ����1***\n "); //��ӡ�˵� 
		printf("***ִ�д�ӡ����2***\n");
		printf("***������0***\n");
		printf("��ѡ������");
		scanf("%d",&m);
		if(m=0)
			break;
		if(m==1){
			printf("�����룬��ź��ı����ݣ�ʹ�ã�������ı�����С��100��\n");
			scanf("%d,%s",&no,str);
			EnPrintTaskQueue(&Q,no,str);
			OutputPrintTask(Q);
		} 
		else{
			//��ҵ����
			DePrintTaskQueue(&Q); 
		}
	}
} 

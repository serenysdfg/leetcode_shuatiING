#include<iostream>
#include<malloc.h>
#include<stdio.h>
using namespace std;
typedef struct node
{
	int x;
	int y;
	struct node *next;
}node;

int main()
{
	int n,i,x=0,y=0;
	node *p,*q,*r;
	p=q=(node *)malloc(sizeof(node));
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		cin>>q->x;
		cin>>q->y;	
		
		r=q;
		q=q->next;
	/*
		r=(node *)malloc(sizeof(node));
		q->next=r;
		q=r;*/
	}
	q->next=0;
	q->x=0;
	q->y=0;
	while(p!=0)
	{
		x+=p->x;
		y+=p->y;
		p=p->next;
	}
	printf("%d+%di",x,y);
	return 0;
}



/*#include<iostream>
#include<cstdio>
#include<malloc.h> 
using namespace std;
typedef struct Node{
	int data;
	struct Node *next;
}LinkList;
int main(){
	int i,n,a;
	while(scanf("%d",&n)!=EOF){	
		LinkList *head,*pre,*p,*newNode;
		head=(LinkList*)malloc(sizeof(LinkList));
		head->next=NULL;
		//输入数据
		for(int i=0;i<n;i++){
			newNode=(LinkList*)malloc(sizeof(LinkList));
			scanf("%d",&newNode->data);
			//升序排序
			pre=head;
			p=head->next;
			//找到插入位置
			while(p){//一个个往后 
				if(newNode->data<p->data){
					break;
				}
				pre=p;
				p=p->next;
			}
			//插入新节点
			newNode->next=p;
			pre->next=newNode; 			
		} 
		//输出
		p=head->next;
		printf("%d",p->data);
		while(p->next){
			p=p->next;
			printf(" %d",p->data);
		}
		printf("\n");
	}
	
	return 0;
}
*/

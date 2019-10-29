#include<stdio.h>
#include<stdlib.h>

#define MAXSIZE 10 
int queue[MAXSIZE];
int front=-1;
int rear=-1;
//�����������
void addqueue(int value){
	rear=(rear+1)%MAXSIZE;
	if(front==rear)
		printf("The wueue is full!!");
	else
		queue[rear]=value; 
		
} 
//����������ݣ��Ӻ�ˣ�
int rear_delqueue(){
	int temp;
	if(front==rear)
		return -1;
	temp=queue[rear];
	rear--;
	if(rear<0&&front!=-1)
		rear=MAXSIZE-1;
	return temp;
} 

//����������ݣ���ǰ�ˣ�
int front_delqueue() {
	if(front==rear)
		return -1;
	front++;
	if(front==MAXSIZE)
		front=0;
	return queue[front];
}

//������
int main(){
	int select;
	int output_queue[5];
	
	int input_queue[5]={5,4,3,2,1};
	int temp,position=0,i;
	for(i=0;i<5;i++){
		addqueue(input_queue[i]);
	}
	printf("The original  queue order :");
	for(i=0;i<5;i++){
		printf("[%d]",input_queue[i]);
	}
	printf("\n");
	while(front!=rear){
		printf("(1)From 'Front-end'\n");
		printf("(2)From 'Rear-end'\n");
		printf("please select  one=>");
		scanf("%d",&select);
		
		switch(select){
			case 1:
				temp=front_delqueue();
				output_queue[position++]=temp;
				break; 
 			case 2:
				temp=rear_delqueue();
				output_queue[position++]=temp;
				break; 		}
	}
	printf("\n the output order��");
	for(i=0;i<5;i++){
		printf("[%d]",output_queue[i]);		
	} 
	printf("\n");
	return 0;
} 

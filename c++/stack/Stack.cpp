//4.2.3˳��ջӦ�þ���
#include<stdio.h>
#include<stdlib.h> 
//���Ͷ���
typedef char DataType;
#include "SeqStack.h"
void main(){
	SeqStack S;
	int i;
	DataType a[]={'A','B','C','D','E','F'};
	dATAtYPE E;
	InitStack(&S);//��ַ
	for(i=0;i<sizeod(a)/sizeof(a[0]);i++) { //���ν�ջ 
		if(PushStack(&S,a[i])==0){
			printf("ջ���������ܽ�ջ��");
			return;
		}
	}
	printf("���γ�ջ��Ԫ���ǣ� ");
	if(PopStack(&S,&e)==1) //Ԫ��F��ջ 
		printf("%4c",e);
	if(PopStack(&S,&e)==1)
		printf("%4c",e);
	printf("\n");
	printf("��ǰ��ջ��Ԫ���ǣ� ");
	if(GetTop(S,&e)==0){
		printf("ջ�ѿգ�");
		return;
	} 
	else
		printf("%4c\n",e);
	printf("��Ԫ�أ�G��H������ջ��\n");
	if(PushStack(&S,'G')==0){
		printf("ջ���������ܽ�ջ��");
		return;
	}
	if(PushStack(&S,'H')==0){
		printf("ջ���������ܽ�ջ");
		return;
	}
	printf("��ǰջ�е�Ԫ�ظ����ǣ�%d\n",StackLength(S));
	printf("��ջ��Ԫ�س�ջ����ջ�������ǣ�\n");
	while(!StackEmpty(S)){
		PopStack(&S,&e);
		printf("%4c",e);
	} 
	printf("\n");
	 

	
}


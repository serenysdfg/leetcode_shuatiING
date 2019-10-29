#include<stdio.h> 
#include <string.h>
#define Max_Size 100
#define SUCCESS 1
#define FAILURE 0
typedef char ElemType;
typedef struct{
	ElemType stack[Max_Size];
	int top;
}SeqStack;

void InitStack(SeqStack *S){
	S->top=0;
} 

/*�ж��Ƿ�Ϊ�գ��շ���0*/
int IsStackEmpty(SeqStack *S){
	if(S->top<=0) //�ǿ� 
		return 1;
	else
		return 0; 
}

//ѹջ
int StackPush(SeqStack *S,ElemType x){
	if(S->top>=Max_Size){
		printf("ջ�������޷����룡\n");
		return 0;
	}
	else{
		S->stack[S->top]=x;
		S->top++;
		return 1;
	}
} 
int StackPop(SeqStack *S,ElemType *d){
	if(S->top<=0){
		printf("��ջ�ѿգ�������Ԫ�س�ջ��\n");
		return 0;
	}
	else{
		S->top--;
		*d=S->stack[S->top];
		return 1;
	}
}
//ȡ˳��ջS�ĵ�ǰջ��Ԫ��ֵ������d�����ɹ�����1�����򷵻�0
int GetTop(SeqStack *S,ElemType *d){
	if(S->top<=0){
			printf("��ջ�ѿգ�\n");
			return 0;
		
	}
	else{
		*d=S->stack[S->top-1];
		return 1;
	}

} 

//����ƥ��ļ���
int Bracket_Matching(char *str){
	char *p;
	char tmp;
	SeqStack S;
	InitStack(&S);
	p=str;
	while(*p!='\0'){
		//������ѹջ
		if(*p=='('  || *p=='['){
			StackPush(&S,*p);
		} 
		else if(*p==')'){
			GetTop(&S,&tmp);
			if(tmp=='('){
				StackPop(&S,&tmp);
			}
			else{
				return FAILURE;
			}
		} 
		else if(*p==']'){
			//��ջ��Ԫ�رȽϣ�ƥ����ջ
			GetTop(&S,&tmp);
			if(tmp=='['){
				StackPop(&S,&tmp);
			} 
			else{
				return FAILURE;
			}
			
		}
		p++;
	}
	//ѭ�������󣬣�ջӦ��Ϊ�գ����������
	if(!IsStackEmpty(&S)){
		return FAILURE;
	} 
	return SUCCESS;
} 
int main(){
	int ret;
	char str[Max_Size];
	while(1){
		printf("\n�������ַ�awsn ��\n");
		gets(str);
		if(!strcmp(str,"0")){
			break;
		}
		ret=Bracket_Matching(str);
		printf("%d\n",ret);
	}
}


#include<stdio.h> 
#include<string.h>
#define Max_Size 100
typedef char ElemType;
typedef struct{
	ElemType stack[Max_Size];
	int top;
}SeqStack;

/*��ʼ��˳��ṹջS*/
void InitStack(SeqStack *S){
	S->top=0;
} 
/*�ж�˳��ջ�Ƿ�Ϊ�գ��ǿ��򷵻�0.�����򷵻�1*/ 
int IsStackEmpty(SeqStack *S){
	if(S->top<=0)
		return 1;
	
	else
			return 0;
}

/*��xѹ��ջS��ѹջ�ɹ�����������1�����򷵻�0*/
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

/*��ջ����ջ����ֵ������d����ջ�ɹ�����������1������������0*/
int StackPop(SeqStack *S,ElemType *d){
	if(S->top<=0){
		printf("ջ�ѿգ�û��Ԫ�ؿ��Գ�ջ��\n");
		return 0;
	}
	else{
		S->top--;
		*d=S->stack[S->top];
		return 1;
		
	}
} 
void Pal(char str[]){  //sereny:����char str[] 
	SeqStack S;char c; int i ,length;
	length=strlen(str);
	InitStack(&S);
	for(i=0;i<length;i++){
		StackPush(&S,str[i]);
	}
	i=0;
	while(IsStackEmpty(&S)==0){
		if(StackPop(&S,&c)==1&&c!=str[i]){
			printf("%s���ǻ��ģ�\n",str);
			return;
		}
		else i++;
	}
	printf("%s�ǻ��ģ�\n",str);
}
int main(){
	char str[Max_Size];
	while(1){
		printf("\n�������ַ�����\n");
		gets(str);
		if(!strcmp(str,"0")) //sereny:������ȣ�����0 
			break;
		Pal(str);
	}
	return 0;
}

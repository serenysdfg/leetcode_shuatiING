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

/*判断是否为空，空返回0*/
int IsStackEmpty(SeqStack *S){
	if(S->top<=0) //非空 
		return 1;
	else
		return 0; 
}

//压栈
int StackPush(SeqStack *S,ElemType x){
	if(S->top>=Max_Size){
		printf("栈已满，无法插入！\n");
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
		printf("堆栈已空，无数据元素出栈！\n");
		return 0;
	}
	else{
		S->top--;
		*d=S->stack[S->top];
		return 1;
	}
}
//取顺序栈S的当前栈顶元素值到参数d，若成功返回1，否则返回0
int GetTop(SeqStack *S,ElemType *d){
	if(S->top<=0){
			printf("堆栈已空！\n");
			return 0;
		
	}
	else{
		*d=S->stack[S->top-1];
		return 1;
	}

} 

//括号匹配的检验
int Bracket_Matching(char *str){
	char *p;
	char tmp;
	SeqStack S;
	InitStack(&S);
	p=str;
	while(*p!='\0'){
		//做括号压栈
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
			//与栈顶元素比较，匹配后出栈
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
	//循环结束后，，栈应该为空，。否则出错
	if(!IsStackEmpty(&S)){
		return FAILURE;
	} 
	return SUCCESS;
} 
int main(){
	int ret;
	char str[Max_Size];
	while(1){
		printf("\n请输入字符awsn 串\n");
		gets(str);
		if(!strcmp(str,"0")){
			break;
		}
		ret=Bracket_Matching(str);
		printf("%d\n",ret);
	}
}


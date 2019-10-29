#include<stdio.h> 
#include<string.h>
#define Max_Size 100
typedef char ElemType;
typedef struct{
	ElemType stack[Max_Size];
	int top;
}SeqStack;

/*初始化顺序结构栈S*/
void InitStack(SeqStack *S){
	S->top=0;
} 
/*判断顺序栈是否为空，非空则返回0.。空则返回1*/ 
int IsStackEmpty(SeqStack *S){
	if(S->top<=0)
		return 1;
	
	else
			return 0;
}

/*将x压入栈S，压栈成功，函数返回1，否则返回0*/
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

/*出栈，将栈顶赋值给参数d，出栈成功，函数返回1，否则函数返回0*/
int StackPop(SeqStack *S,ElemType *d){
	if(S->top<=0){
		printf("栈已空，没有元素可以出栈！\n");
		return 0;
	}
	else{
		S->top--;
		*d=S->stack[S->top];
		return 1;
		
	}
} 
void Pal(char str[]){  //sereny:传参char str[] 
	SeqStack S;char c; int i ,length;
	length=strlen(str);
	InitStack(&S);
	for(i=0;i<length;i++){
		StackPush(&S,str[i]);
	}
	i=0;
	while(IsStackEmpty(&S)==0){
		if(StackPop(&S,&c)==1&&c!=str[i]){
			printf("%s不是回文！\n",str);
			return;
		}
		else i++;
	}
	printf("%s是回文！\n",str);
}
int main(){
	char str[Max_Size];
	while(1){
		printf("\n请输入字符串：\n");
		gets(str);
		if(!strcmp(str,"0")) //sereny:两者相等，返回0 
			break;
		Pal(str);
	}
	return 0;
}

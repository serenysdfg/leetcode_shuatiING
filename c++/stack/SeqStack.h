//初始化栈 
void InitStack(SeqStack *S){
	S->top=0;//把栈顶的指针置为0 
}
//判断栈是否为空
int StackEmpty(SeqStack S)
{
	if(S.top==0)
		return 1;
	else
		return 0;
} 
//取栈顶元素
int GetTop(SeqStack S,DataType *e){
	if(S.top<=0){
		printf("栈已经空！\n");
		return 0;
	}
	else{
		*e=S.stack[S.top-1];
		return1;
	}
} 
//入栈
int PushStack(SeqStack *S,DataType e){
	if(S->top>=StackSize){
		printf("栈已满，不能再将元素进栈！\n");
		return 0;
	}
	else{
		S->stack[S->top]=e;
		S->top++;
		return 1;
	}
} 
//出栈
int PopStack(SeqStack *S,DataType *e){
	if(S->top==0){
		printf("栈为空，不能进行出栈操作！\n");
		return 0;
	}
	else{
		S->top--;
		*e=S->stack[S->top];
		return 1;
	}
} 

//求栈的长度
int StackLength(SeqStack S){
	return S.top;
} 
//清空栈
void ClearStack(SeqStack *S){
	S->top=0;
} 

 


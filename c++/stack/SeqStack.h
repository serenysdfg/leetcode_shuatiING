//��ʼ��ջ 
void InitStack(SeqStack *S){
	S->top=0;//��ջ����ָ����Ϊ0 
}
//�ж�ջ�Ƿ�Ϊ��
int StackEmpty(SeqStack S)
{
	if(S.top==0)
		return 1;
	else
		return 0;
} 
//ȡջ��Ԫ��
int GetTop(SeqStack S,DataType *e){
	if(S.top<=0){
		printf("ջ�Ѿ��գ�\n");
		return 0;
	}
	else{
		*e=S.stack[S.top-1];
		return1;
	}
} 
//��ջ
int PushStack(SeqStack *S,DataType e){
	if(S->top>=StackSize){
		printf("ջ�����������ٽ�Ԫ�ؽ�ջ��\n");
		return 0;
	}
	else{
		S->stack[S->top]=e;
		S->top++;
		return 1;
	}
} 
//��ջ
int PopStack(SeqStack *S,DataType *e){
	if(S->top==0){
		printf("ջΪ�գ����ܽ��г�ջ������\n");
		return 0;
	}
	else{
		S->top--;
		*e=S->stack[S->top];
		return 1;
	}
} 

//��ջ�ĳ���
int StackLength(SeqStack S){
	return S.top;
} 
//���ջ
void ClearStack(SeqStack *S){
	S->top=0;
} 

 


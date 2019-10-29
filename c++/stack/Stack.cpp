//4.2.3顺序栈应用举例
#include<stdio.h>
#include<stdlib.h> 
//类型定义
typedef char DataType;
#include "SeqStack.h"
void main(){
	SeqStack S;
	int i;
	DataType a[]={'A','B','C','D','E','F'};
	dATAtYPE E;
	InitStack(&S);//地址
	for(i=0;i<sizeod(a)/sizeof(a[0]);i++) { //依次进栈 
		if(PushStack(&S,a[i])==0){
			printf("栈已满，不能进栈！");
			return;
		}
	}
	printf("依次出栈的元素是： ");
	if(PopStack(&S,&e)==1) //元素F出栈 
		printf("%4c",e);
	if(PopStack(&S,&e)==1)
		printf("%4c",e);
	printf("\n");
	printf("当前的栈顶元素是： ");
	if(GetTop(S,&e)==0){
		printf("栈已空！");
		return;
	} 
	else
		printf("%4c\n",e);
	printf("将元素，G，H依次入栈。\n");
	if(PushStack(&S,'G')==0){
		printf("栈已满，不能进栈！");
		return;
	}
	if(PushStack(&S,'H')==0){
		printf("栈已满，不能进栈");
		return;
	}
	printf("当前栈中的元素个数是：%d\n",StackLength(S));
	printf("将栈中元素出栈，出栈的序列是：\n");
	while(!StackEmpty(S)){
		PopStack(&S,&e);
		printf("%4c",e);
	} 
	printf("\n");
	 

	
}


#include<stdio.h>
#include<string.h>
struct Node{
	Node *lchild;
	Node *rchild;
	char c;//结点字符信息 
}Tree[50];

int loc;//静态内存中已经分配的节点个数 
Node *creat(){
	Tree[loc].lchild=Tree[loc].rchild=NULL;
	return &Tree[loc++];//返回指针 ，且loc累加 
} 
char str1[30],str2[30];//保存前序遍历和中序遍历字符串
void postOrder(Node *T){
	if(T->lchild!=NULL){
		postOrder(T->lchild);
	}
	if(T->rchild!=NULL){
		postOrder(T->rchild);
	}
	printf("%c",T->c);
} 
Node *build(int s1,int e1,int s2,int e2){
	Node *ret=creat();//为该树节点申请空间
	ret->c=str1[s1];//该节点字符为前序遍历中的第一个字符
	int rootIdx;
	for(int i=s2;i<=e2;i++){
		if(str2[i]==str1[s1]){
			rootIdx=i;
			break;
		}
	} 
	if(rootIdx!=s2) //若左子树不为空
	{
		ret->lchild=build(s1+1,s1+(rootIdx-s2),s2,rootIdx-1);//递归还原左子树 
	 } 
	 	if(rootIdx!=e2) //若左子树不为空
	{
		ret->rchild=build(s1+(rootIdx-s2)+1,e1,rootIdx+1,e2);//递归还原右子树 
	 }
	 return ret; 
}
int main(){
	while(scanf("%s",str1)!=EOF){
		scanf("%s",str2);
		loc=0;
		int L1=strlen(str1);
		int L2=strlen(str2);//计算两个字符串长度
		Node *T=build(0,L1-1,0,L2-1);
		postOrder(T);//后序遍历
		printf("\n");
		 
	}
	return 0;
}

#include<stdio.h>
#include<string.h>
struct Node{
	Node *lchild;
	Node *rchild;
	char c;//����ַ���Ϣ 
}Tree[50];

int loc;//��̬�ڴ����Ѿ�����Ľڵ���� 
Node *creat(){
	Tree[loc].lchild=Tree[loc].rchild=NULL;
	return &Tree[loc++];//����ָ�� ����loc�ۼ� 
} 
char str1[30],str2[30];//����ǰ���������������ַ���
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
	Node *ret=creat();//Ϊ�����ڵ�����ռ�
	ret->c=str1[s1];//�ýڵ��ַ�Ϊǰ������еĵ�һ���ַ�
	int rootIdx;
	for(int i=s2;i<=e2;i++){
		if(str2[i]==str1[s1]){
			rootIdx=i;
			break;
		}
	} 
	if(rootIdx!=s2) //����������Ϊ��
	{
		ret->lchild=build(s1+1,s1+(rootIdx-s2),s2,rootIdx-1);//�ݹ黹ԭ������ 
	 } 
	 	if(rootIdx!=e2) //����������Ϊ��
	{
		ret->rchild=build(s1+(rootIdx-s2)+1,e1,rootIdx+1,e2);//�ݹ黹ԭ������ 
	 }
	 return ret; 
}
int main(){
	while(scanf("%s",str1)!=EOF){
		scanf("%s",str2);
		loc=0;
		int L1=strlen(str1);
		int L2=strlen(str2);//���������ַ�������
		Node *T=build(0,L1-1,0,L2-1);
		postOrder(T);//�������
		printf("\n");
		 
	}
	return 0;
}

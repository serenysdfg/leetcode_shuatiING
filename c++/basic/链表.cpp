/** 
**����ڵ�Ķ��� 
*/  
typedef struct  Node{  
int data;//������  
struct Node * PNext;//ָ���򣬴����һ���ڵ�ĵ�ַ  
} Node ,* PNode ;  
/** 
**�������� 
*/  
PNode create_list()  
{  
    int len,i;  
    printf("����������ĳ��ȣ�len=\n");  
    scanf("%d",&len);  
    PNode PHead=malloc(sizeof(Node));  
    PHead->PNext=NULL;  
    PNode PTail=PHead;//PTail����Զָ��β�ڵ��ָ��  
    for(i=0;i<len;i++)  
    {  
        int val;  
        printf("������� %d ��Ԫ�ص�ֵ��", i+1);  
        scanf("%d",&val);  
        PNode PNew=malloc(sizeof(Node));  
        PNew->data=val;  
        PNew->PNext=NULL;  
        PTail->PNext=PNew;  
        PTail=PNew;  
    }  
    return PHead;  
  
}  
  
/** 
**��������б��� 
*/  
void traverse(PNode pHead)  
{  
   PNode p=pHead->PNext;  
   while(p!=NULL)  
   {  
       printf("%d    ",p->data);  
       p=p->PNext;  
   }  
   printf("\n");  
}  
/** 
*�ж������Ƿ�Ϊ�� 
*/  
  
bool isempty(PNode pHead)  
{  
    if(NULL==pHead->PNext)  
    {  
            return true;  
    }else{  
    return false;  
    }  
}  
  
/** 
**��ȡ����ĳ��� 
*/  
int list_num (PNode pHead)  
{  
  int num=0;  
  PNode p=pHead->PNext;  
  while(p!=NULL)  
  {  
      num++;  
      p=p->PNext;  
  }  
  return  num;  
}  
  
/** 
*�������в���Ԫ�� 
*/  
bool insert_list(PNode pHead,int val ,int pos){  
//��Ҫ�ҵ���pos��λ�ã�������Ҫ�ж����λ��pos�Ƿ�Ϸ�  
 //i��p��ָ�ڵ��λ�ã����Դ�һ��ʼ��ΪʲôҪpos-1�أ���Ϊ�õ���while ��i=pos-1ʱ����ѭ��  
 int i=0;  
 PNode p=pHead;  
 while(NULL!=p&&i<pos-1)  
 {  
     i++;  
     p=p->PNext;  
 }  
//�������λ�ù�����ôP=NULL,  
//��������λ����0���߸�������ôi>pos-1  
if(i>pos-1||NULL==p)  
 {  
     printf("����λ�ò��Ϸ�\n");  
     return false;  
 }  
PNode PNew=malloc(sizeof(PNode));  
PNew->data=val;  
PNode temp=p->PNext;  
p->PNext=PNew;  
PNew->PNext=temp;  
return true;  
}  
  
/** 
**��������ɾ���ڵ� 
*/  
delete (PNode PHead,int pos , int * pval)  
{  
    int i=0;  
    PNode p=PHead;  
    //����Ҫɾ��p����Ľڵ㣬����p����ָ�����һ���ڵ� p->next!=NULL  
    while(p->PNext!=NULL&&i<pos-1){  
  
        p=p->PNext;  
        i++;  
    }  
    if(i>pos-1||p->PNext==NULL)  
    {  
        printf("ɾ��λ�ò��Ϸ�\n");  
     return false;  
    }  
   PNode temp=p->PNext;  
   p->PNext=temp->PNext;  
   free(temp);  
  
  
  
}  
int main()  
{  
  
 PNode PHead= create_list();  
if(isempty(PHead))  
printf("����Ϊ��\n");  
printf("����ĳ���Ϊ��%d\n",list_num(PHead));  
traverse(PHead);  
//insert_list(PHead,55,1);  
int val;  
 delete(PHead,6,&val);  
traverse(PHead);  
return 0;  
}  

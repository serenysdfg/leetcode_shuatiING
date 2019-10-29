   //�Ŷ�oj��1201 
   
   
   
    #include <iostream>    
    using namespace std;    
    #include <stdio.h>    
    #include <stdlib.h>    
        
    typedef struct BiTNode    
    {    
        int value;    
        struct BiTNode *lchild,*rchild;    
    }*BiTree;    
        
    bool LT(int a,int b)  //LessThanС��    
    {    
        if(a<b)    
            return true;    
        else    
            return false;    
    }    
    /*  
    �ڸ�ָ��root��ָ��Ķ����������еݹ�ز�����ؼ��ֵ���data������Ԫ�أ������ҳɹ�����ָ��pָ�������Ԫ�ؽ�㣬������true��  
    ����ָ��pָ�����·���Ϸ��ʵ����һ����㲢����falseָ�룬ָ��fָ��root��˫�ף����ʼ����ֵNULL  
    */    
    bool SearchBST(BiTree root,int data,BiTree f,BiTree &p)    
    {    
        if(!root)    
        {    
            p=f;    
            return false;    
        }    
        else if(data==root->value)    
        {    
            p=root;    
            return true;    
        }    
        else if(data<root->value)    
            return SearchBST(root->lchild,data,root,p);    
        else if(data>root->value)    
            return SearchBST(root->rchild,data,root,p);    
    }    
        
    //������������root�в����ڹؼ��ֵ���data������Ԫ��ʱ������data���˺�������Ƶ�ʸߣ��������ó�inline  
    inline void InsertBST(BiTree &root,int data)     //rootΪ������ָ��    
    {      
        BiTree p,s;    
        if(!SearchBST(root,data,NULL,p))    //���Ҳ��ɹ�    
        {    
            s=(struct BiTNode *)malloc(sizeof(BiTNode));    
            s->value=data;    
            s->lchild=s->rchild=NULL;    
            if(p==NULL)    //����������Ϊ�յ�ʱ�򣬱�������*sΪ�µĸ����    
                root=s;    
            else if(LT(data,p->value))           //������*sΪ����    
                p->lchild=s;    
            else           //������*sΪ�Һ���    
                p->rchild=s;    
        }    
        return ;    
    }    
    void PreOrderTraverse(BiTree root)    //�������    
    {    
        if(root)    
        {    
            printf("%d ",root->value);    
            PreOrderTraverse(root->lchild);    
            PreOrderTraverse(root->rchild);    
        }    
    }    
    void InOrderTraverse(BiTree root)    //�������    
    {    
        if(root)    
        {    
            InOrderTraverse(root->lchild);    
            printf("%d ",root->value);    
            InOrderTraverse(root->rchild);    
        }    
    }    
    void PostOrderTraverse(BiTree root)    //�������    
    {    
        if(root)    
        {    
            PostOrderTraverse(root->lchild);    
            PostOrderTraverse(root->rchild);    
            printf("%d ",root->value);    
        }    
    }    
    void DeleteBST(BiTree root)  //�ͷŶ�����ռ�õ��ڴ�ռ�  
    {    
        if(root)    
        {    
            DeleteBST(root->lchild);    //�ͷ�������    
            DeleteBST(root->rchild);    //�ͷ�������    
            free(root);        //�ͷŸ����    
        }    
    }    
    int main(void)    
    {    
        int i,a[101],n;    
        BiTree root;    
        while(scanf("%d",&n)!=EOF)    
        {    
            root=NULL;    
            for(i=1;i<=n;i++)    
            {    
                scanf("%d",&a[i]);    
                InsertBST(root,a[i]);    
            }    
            PreOrderTraverse(root);    
            printf("\n");    
            InOrderTraverse(root);    
            printf("\n");    
            PostOrderTraverse(root);    
            printf("\n");    
            DeleteBST(root);    
        }    
        return 0;    
    }  

   //九度oj：1201 
   
   
   
    #include <iostream>    
    using namespace std;    
    #include <stdio.h>    
    #include <stdlib.h>    
        
    typedef struct BiTNode    
    {    
        int value;    
        struct BiTNode *lchild,*rchild;    
    }*BiTree;    
        
    bool LT(int a,int b)  //LessThan小于    
    {    
        if(a<b)    
            return true;    
        else    
            return false;    
    }    
    /*  
    在根指针root所指向的二叉排序树中递归地查找其关键字等于data的数据元素，若查找成功，则指针p指向该数据元素结点，并返回true，  
    否则指针p指向查找路径上访问的最后一个结点并返回false指针，指针f指向root的双亲，其初始调用值NULL  
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
        
    //当二叉排序树root中不存在关键字等于data的数据元素时，插入data，此函数调用频率高，所以设置成inline  
    inline void InsertBST(BiTree &root,int data)     //root为传引用指针    
    {      
        BiTree p,s;    
        if(!SearchBST(root,data,NULL,p))    //查找不成功    
        {    
            s=(struct BiTNode *)malloc(sizeof(BiTNode));    
            s->value=data;    
            s->lchild=s->rchild=NULL;    
            if(p==NULL)    //二叉排序树为空的时候，被插入结点*s为新的根结点    
                root=s;    
            else if(LT(data,p->value))           //被插结点*s为左孩子    
                p->lchild=s;    
            else           //被插结点*s为右孩子    
                p->rchild=s;    
        }    
        return ;    
    }    
    void PreOrderTraverse(BiTree root)    //先序遍历    
    {    
        if(root)    
        {    
            printf("%d ",root->value);    
            PreOrderTraverse(root->lchild);    
            PreOrderTraverse(root->rchild);    
        }    
    }    
    void InOrderTraverse(BiTree root)    //中序遍历    
    {    
        if(root)    
        {    
            InOrderTraverse(root->lchild);    
            printf("%d ",root->value);    
            InOrderTraverse(root->rchild);    
        }    
    }    
    void PostOrderTraverse(BiTree root)    //后序遍历    
    {    
        if(root)    
        {    
            PostOrderTraverse(root->lchild);    
            PostOrderTraverse(root->rchild);    
            printf("%d ",root->value);    
        }    
    }    
    void DeleteBST(BiTree root)  //释放二叉树占用的内存空间  
    {    
        if(root)    
        {    
            DeleteBST(root->lchild);    //释放左子树    
            DeleteBST(root->rchild);    //释放右子树    
            free(root);        //释放根结点    
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

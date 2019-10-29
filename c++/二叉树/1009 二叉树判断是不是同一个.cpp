    //九度oj：1009
 
	#include <iostream>  
    #include <string.h>  
    using namespace std;  
      
    struct Node{  
        Node* left ;  
        Node* right ;  
        char data ;  
        Node():left(NULL),right(NULL),data('*'){}  
    };  
      
    //插入有序树  
    void insertSortTree(Node * root, char data){  
        Node * p = root ;  
        Node * q = new Node ;  
        q->data = data ;  
        while(1){  
            if(p->data>data&&p->left)p=p->left;  
            else if(p->data<data&&p->right)p=p->right;  
            else if(p->data>data){  
                p->left = q ;  
                return;  
            }  
            else if(p->data<data){  
                p->right = q ;  
                return;  
            }  
        }  
    }  
    //销毁有序树  
    void destroySortTree(Node * root){  
        Node * p = root ;  
        if(p->left!=NULL)destroySortTree(p->left);  
        if(p->right!=NULL)destroySortTree(p->right);  
        delete p ;  
    }  
    //创建有序树  
    Node * createSortTree(char * datas , int n){  
        if(n<=0)return NULL;  
        Node * root = new Node ;  
        root->data = datas[0];  
        Node * p = root ;  
        for(int i = 1 ; i < n ;i++){  
            insertSortTree(root,datas[i]);  
        }  
        return root ;  
    }  
    //用到的变量  
    char x1[11];int ct1 = 0;  
    char x2[11];int ct2 = 0;  
    //前根序遍历  
    void pre_lst(Node * root,char* x,int* index){  
        if(root)x[(*index)++] = root->data ;  
        if(root->left)pre_lst(root->left,x,index) ;  
        if(root->right)pre_lst(root->right,x,index) ;  
    }  
    //比较前根序列  
    bool cmp(int n){  
        for(int i = 0 ; i < n ; i++){  
            if(x1[i]!=x2[i])return false;  
        }  
        return true ;  
    }  
    int main()  
    {  
        int T ;  
        int n;  
        Node * root1 = NULL;  
        Node * root2 = NULL;  
        int index1 ,index2 ;  
        while(1){  
            cin>>T ;if(T==0)break;  
            cin>>x1 ;  
            ct1 = strlen(x1);  //获取长度，用于比较 
            root1 = createSortTree(x1,ct1);  
            index1 = 0 ;  
            pre_lst(root1,x1,&index1) ;  
            for(int i = 0 ; i < T ; i++ ){  
                cin>>x2 ;  
                ct2 = strlen(x2);  
                root2 = createSortTree(x2,ct2);  
                index2 = 0 ;  
                pre_lst(root2,x2,&index2) ;  
                if(cmp(ct1)){  
                    cout<<"YES"<<endl;  
                }else cout<<"NO"<<endl;  
                destroySortTree(root2) ;  
            }  
            destroySortTree(root1) ;  
      
        }  
      
        return 0;  
    }  

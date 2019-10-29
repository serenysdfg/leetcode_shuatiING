    #include <iostream>  
    #define L 11  
      
    using namespace std;  
      
    typedef struct TNode{  
        int num;  
        struct TNode *child[26];  
        TNode(){  
            num = 0;  
            int i;  
            for(i=0;i<26;i++){  
                child[i] = NULL;  
            }  
        }  
    }TNode;  
      
    void InTree(TNode *root,char word[]);  
    int Find(TNode *root,char word[]);  
      
    int main(void)  
    {  
        int n,m;  
        char word[L];  
        TNode *root = new TNode();  
      
        for(cin>>n;n--;){  
            cin>>word;  
            InTree(root,word);  
        }  
        for(cin>>m;m--;){  
            cin>>word;  
            cout<<Find(root,word)<<endl;  
        }  
        return 0;  
    }  
      
    void InTree(TNode *root,char word[]){  
      
        for(int i=0;word[i];i++){  
            int pos = word[i]-'a';  
            if(root->child[pos]==NULL)  
                root->child[pos] = new TNode();  
            root->child[pos]->num++;  
            root = root->child[pos];  
              
        }  
    }  
      
    int Find(TNode *root,char word[]){  
        for(int i=0;word[i];i++){  
            int pos = word[i] - 'a';  
            if(root->child[pos] == NULL)  
                return 0;  
            root = root->child[pos];  
        }  
        return root->num;  
    }  

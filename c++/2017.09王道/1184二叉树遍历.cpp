#include<iostream>
#include<string>
using namespace std;
struct BNode{//二叉树节点
    BNode(const char d='#'):data(d), left(NULL), right(NULL) {};
    char data;
    BNode* left;
    BNode* right;
};

BNode* constructBinaryTree(const )
      
//根据先序遍历构建一棵二叉树，返回root指针，（不断在左边插入 -我的备注 
BNode* constructBinaryTree(const string& preOrder, unsigned& index){
    if (preOrder.size() == 0 || index == preOrder.size() || preOrder[index] == '#')//若空串或者index超出范围，则返回空指针
        return NULL;
    BNode* T = new BNode(preOrder[index++]);
    T->left = constructBinaryTree(preOrder, index);
    T->right = constructBinaryTree(preOrder, ++index);
    return T;
}
//中序遍历
void mediaOrder(BNode* T){
    if (T != NULL){
        mediaOrder(T->left);
        cout << T->data << " ";
        mediaOrder(T->right);
    }
}
int main(){
    string str;
    while (cin >> str){
        unsigned index = 0;
        BNode* root = constructBinaryTree(str, index);
        mediaOrder(root);
        cout << endl;
    }
    return 0;
}

int main(){
	string str;
	while(cin>>str){
		unsigned index =0;
		
	}
}

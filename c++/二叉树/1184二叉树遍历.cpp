#include<iostream>
#include<string>
using namespace std;
struct BNode{//�������ڵ�
    BNode(const char d='#'):data(d), left(NULL), right(NULL) {};
    char data;
    BNode* left;
    BNode* right;
};

BNode* constructBinaryTree(const )
      
//���������������һ�ö�����������rootָ��
BNode* constructBinaryTree(const string& preOrder, unsigned& index){
    if (preOrder.size() == 0 || index == preOrder.size() || preOrder[index] == '#')//���մ�����index������Χ���򷵻ؿ�ָ��
        return NULL;
    BNode* T = new BNode(preOrder[index++]);
    T->left = constructBinaryTree(preOrder, index);
    T->right = constructBinaryTree(preOrder, ++index);
    return T;
}
//�������
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

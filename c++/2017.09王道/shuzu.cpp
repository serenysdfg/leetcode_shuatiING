#include<iostream>
#include<vector>
using namespace std;
class BinTree:vector<int>
{
    public:
        explicit BinTree(int k=0)//Ĭ�ϳ�ʼ��һ���ܱ���k��Ԫ�صĿ���״����
        {
            assign(k+1,0);//��Ч�±��1��ʼ��0�����߼��ô�
        }
        int lowbit(int k)
        {
            return k&-k;
            //Ҳ��д��x&(x^(x�C1))
        }
        int sum(int k)//���1��Ԫ�ص���n��Ԫ�صĺ�
        {
            return k>0?sum(k-lowbit(k))+(*this)[k]:0;
        }
        int last()//�������һ��Ԫ���±�
        {
            return size()-1;
        }
        void add(int k,int w)//Ϊ�ڵ�k����w
        {
            if(k>last())return;
            (*this)[k]+=w;
            add(k+lowbit(k),w);
        }
};
int main()
{
    BinTree test(123);
    test.add(27,72);
    cout<<test.sum(26)<<' '<<test.sum(27)<<' '<<test.sum(123);
}

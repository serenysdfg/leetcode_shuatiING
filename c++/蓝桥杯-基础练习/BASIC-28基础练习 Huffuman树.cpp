#include<iostream>
#include<queue>
using namespace std;
priority_queue<
int, vector<int>, greater<int> 
> pq; 

//great�����С��������ȶ��� 
//priority_queue<Type, Container, Functional>  Type Ϊ�������ͣ� Container Ϊ�������ݵ�������Functional ΪԪ�رȽϷ�ʽ 

int main() {
  int n;
  cin >> n;
  while (!pq.empty())// ��ն��� 
    pq.pop();
    
    
    
  int x, s;
  for (int i = 0; i < n; i++) {  
    cin >> x; 
    pq.push(x); //ѹ�� 
  } 
  
  int sum = 0; //sum������� 
  while (pq.size() > 1) {  // pq.size()
    s = pq.top();  //ȡ������Ԫ��-��Сֵ 
    pq.pop();//ɾ����С��Ԫ�� 
    s += pq.top(); //pq.pop()
    pq.pop();
    sum += s;
    pq.push(s); //sѹ��ȥ 
  }
  cout << sum << endl;
  } 

#include<iostream>
#include<queue>
using namespace std;
priority_queue<
int, vector<int>, greater<int> 
> pq; 

//great构造从小到大的优先队列 
//priority_queue<Type, Container, Functional>  Type 为数据类型， Container 为保存数据的容器，Functional 为元素比较方式 

int main() {
  int n;
  cin >> n;
  while (!pq.empty())// 清空队列 
    pq.pop();
    
    
    
  int x, s;
  for (int i = 0; i < n; i++) {  
    cin >> x; 
    pq.push(x); //压入 
  } 
  
  int sum = 0; //sum计算费用 
  while (pq.size() > 1) {  // pq.size()
    s = pq.top();  //取队列首元素-最小值 
    pq.pop();//删除最小的元素 
    s += pq.top(); //pq.pop()
    pq.pop();
    sum += s;
    pq.push(s); //s压回去 
  }
  cout << sum << endl;
  } 

#include <iostream>
#include <cmath>
//�������ǰn�������ĳ˻� mod 5000 
using namespace std;
//����Ĵ����ǹؼ�������Ϊ�˷�ֹ��ʱ���Ƚ��п�ƽ��/��֤ʱ�䣬���������������ķ�����


long isPrime(int N);

int main(void){
    int N;    // ��n������     
    cin >> N;
    cout << isPrime(N);
    return 0;
} 

long isPrime(int N){
    int i, j, n = 0;
    long p = 1;
    
   
    for (i = 2;  ; i++){
        for (j = 2; j <sqrt(i); j++){
            if (i % j == 0){
                // ˵���Ǻ���, ������forѭ������ʼ�ж���һ���� 
                break;
            }
        }
        if (j == i){
            n++;
            p = p * i;    
            if (n == N)
                break;
        }       
    }
    p %= 50000;
    return p;
    
}

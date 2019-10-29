#include <iostream>
#include <cmath>
//请你算出前n个质数的乘积 mod 5000 
using namespace std;
//这里的处理是关键，首先为了防止超时，先进行开平方/保证时间，二是利用求素数的方法，


long isPrime(int N);

int main(void){
    int N;    // 第n个质数     
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
                // 说明是合数, 跳出本for循环，开始判断下一个数 
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

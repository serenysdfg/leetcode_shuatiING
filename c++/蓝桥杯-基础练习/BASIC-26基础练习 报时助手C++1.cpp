#include<iostream>  
  
using namespace std;  
  
string  n[100]={"zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven",  
                "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty",  
                "thirty","forty","fifty"};  
  
void ass(int num){  
    int a=num/10;  
    int b=num%10;  
    if(num<=20){  
        cout<<n[num];  
    }  
    else{  
        cout<<n[a+18];  
        if(b!=0){  
            cout<<" "<<n[b];  
        }  
    }  
}  
  
void time_ass(int hour,int minu){  
    if(minu==0){  
        ass(hour);  
        cout<<" o'clock"<<endl;  
    }  
    else{  
        ass(hour);  
        cout<<" ";  
        ass(minu);  
        cout<<endl;  
    }  
}  
  
int main(){  
    int h,m;  
    cin>>h>>m;  
    time_ass(h,m);  
    return 0;  
}  

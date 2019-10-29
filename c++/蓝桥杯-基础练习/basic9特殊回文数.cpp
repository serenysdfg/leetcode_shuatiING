#include<iostream>
using namespace std;
int main(){
	int n,a,b,c,t;
	cin>>n;
	for(a=1;a<10;a++){
		for(b=0;b<10;b++){
			for(c=0;c<10;c++){
				t=10001*a+1010*b+100*c;
				if(a*2+b*2+c==n){
					cout<<t<<endl;
				}
			}
		} 
	}
	for(a=1;a<10;a++){
		for(b=0;b<10;b++){
			for(c=0;c<10;c++){
				t=100001*a+10010*b+1100*c;
				if(a*2+b*2+2*c==n){
					cout<<t<<endl;
				}
			}
		} 
	}
	return 0;
}

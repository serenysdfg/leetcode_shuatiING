#include<stdio.h>
#include<iostream>
using namespace std;
//第一个和第四个相等。。思路 
int main(){
	for(int a=1;a<10;a++){
		for(int b=0;b<10;b++){
			for(int c=0;c<10;c++){
				for(int d=0;d<10;d++){
					if(a==d&&b==c){
						cout<<a*1000+b*100+c*10+d<<endl;
					}
				}
			}
		}
	}
	return 0;
	
}

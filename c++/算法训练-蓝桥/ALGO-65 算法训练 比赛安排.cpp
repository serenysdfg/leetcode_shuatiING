#include <iostream> 
#include <string>
#include <stdio.h>
using namespace std;
const int N=1000;
bool bArrange[N][N];
int main(){
	int n;
	cin>>n;
	int row=(1<<n);//*2^n几天-1 
	int volumn=1<<(n-1);//每天场数 
	for(int i=0;i<row-1;i++){
		cout<<"<"<<i+1<<">"<<"1-"<<i+2;//<1>
		bool isArrange[N]={false};
		isArrange[1]=isArrange[i+2]=true;
		bArrange[1][i+2]=bArrange[i+2][1]=true;//比完设为1 
		for(int j=1;j<volumn;j++){
			int a;
			for(a=2;a<row;a++)
				if(isArrange[a]==false)
					break;
			for(int b=a+1;b<=row;b++){
				if(bArrange[a][b]==false&&isArrange[b]==false)
				{
					bArrange[a][b]=bArrange[b][a]=true;
					isArrange[a]=isArrange[b]=true;
					cout<<" "<<a<<"-"<<b;
					break;
				}
			}

		}
		cout<<endl;
	}
		return 0;
}


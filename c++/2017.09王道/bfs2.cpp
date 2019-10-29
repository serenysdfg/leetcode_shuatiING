#include<stdio.h>
#include<queue>
usng namespace std;
struct N{
	int a,b,c;
	int t;
}; 
queue<N> Q;
bool mark[101][101][101];
void AtoB(int &a,int sa,int &b,int sb)//&a,b为容积。sa为被子体积
{
	if(sb-b>=a){//a全部倒入 
		b+=a;
		a=0
	}
	else{//不能全部倒入，倒满 
		a-=sb-b;
		b=sb;	
	}
 } 
 int BFS(int s ,int n,int m){
 	while(Q.empty()==false){
 		N now=Q.front();//拿出对头的状态
		Q.pop();
		int a,b,c;
		a=now.a;
		b=now.b;
		c=now.c;//重置 
		AtoB(a,s,b,n);//a-b
		if(mark[a][b][c]==false){
			mark[a][b][c]=true;
			N tmp;
			tmp.a=a;
			tmp.b=b;
			tmp.c=c;
			tmp.t=now.t+1;
			if(a==s/2&&b=s/2) return tmp.t;
			if(c==s/2&&b=s/2) return tmp.t;
			if(a==s/2&&c=s/2) return tmp.t;
			Q.push(tmp);
			
		}
		
		
		a=now.a;
		b=now.b;
		c=now.c;//重置 
	 	AtoB(b,n,a,s);//b-a
	 	....
	 	//a-c;c-a;c-b;b-c
	 }
 }
int main(){
	int s,n,m;
	while(scanf("%d%d%d",&s,&n,&m)!=EOF){
		if(s==0) break;//若s=0则n,m为0则退出
		if(s%2==1) {
			puts("NO");
			continue;		
		}
		for(int i=0;i<s;i++){
			for(int j=0;j<n;j++){
				for(int k=0;k<s;k++){
					mark[i][j][k]=false;
				}
			}
		}//初始化状态
		N tmp;
		tmp.a=s;
		tmp.b=0;
		tmp.c=0 ;
		tmp.t=0//初始时状态
		while（Q.empty()==false) Q.pop();//清空队列中的状态
		Q.push(tmp) ;
		mark[s][0][0]=true;//初始状态
		int rec=BFS(s,n,m);//搜素
		if(rec==-1) pus("no");
		else printf("%d\n",rec);//否则输出答案 
		 
		
	}
	return 0； 
}

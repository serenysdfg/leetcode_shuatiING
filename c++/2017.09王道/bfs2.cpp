#include<stdio.h>
#include<queue>
usng namespace std;
struct N{
	int a,b,c;
	int t;
}; 
queue<N> Q;
bool mark[101][101][101];
void AtoB(int &a,int sa,int &b,int sb)//&a,bΪ�ݻ���saΪ�������
{
	if(sb-b>=a){//aȫ������ 
		b+=a;
		a=0
	}
	else{//����ȫ�����룬���� 
		a-=sb-b;
		b=sb;	
	}
 } 
 int BFS(int s ,int n,int m){
 	while(Q.empty()==false){
 		N now=Q.front();//�ó���ͷ��״̬
		Q.pop();
		int a,b,c;
		a=now.a;
		b=now.b;
		c=now.c;//���� 
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
		c=now.c;//���� 
	 	AtoB(b,n,a,s);//b-a
	 	....
	 	//a-c;c-a;c-b;b-c
	 }
 }
int main(){
	int s,n,m;
	while(scanf("%d%d%d",&s,&n,&m)!=EOF){
		if(s==0) break;//��s=0��n,mΪ0���˳�
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
		}//��ʼ��״̬
		N tmp;
		tmp.a=s;
		tmp.b=0;
		tmp.c=0 ;
		tmp.t=0//��ʼʱ״̬
		while��Q.empty()==false) Q.pop();//��ն����е�״̬
		Q.push(tmp) ;
		mark[s][0][0]=true;//��ʼ״̬
		int rec=BFS(s,n,m);//����
		if(rec==-1) pus("no");
		else printf("%d\n",rec);//��������� 
		 
		
	}
	return 0�� 
}

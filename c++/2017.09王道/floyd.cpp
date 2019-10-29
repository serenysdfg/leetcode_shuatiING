#include<stdio.h>

int ans[101][101];

int main(){
	int n,m;
	while((scanf("%d%d",&m,&n))!=EOF){
		if(n==0&&m==0) break;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				ans[i][j]=-1;//对领接矩阵最小化 
			}
			 ans[i][i]=0;//自己到自己伟0 
		}
	   
	
	
	while(m--){
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		ans[a][b]=ans[b][a]=c;//对邻接矩阵赋值，由于是无向图，该赋值要进行两次 
	} 
	for(int k=1;k<n;k++){
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(ans[i][k]==-1||ans[k][j]==-1) continue; //若两值中不能通过k链接 
				if(ans[i][j]==-1||ans[i][k]+ans[k][j]<ans[i][j]) ans[i][j]=ans[i][k]+ans[k][j];
			}
			
		}
	} 
	printf("%d\n",ans[1][n]);//循环结束后输出答案 
	return 0; 
	}
}

#include<stdio.h>
#include<queue>
using namespace std;
bool mark[50][50][50] ;//标记数组
int maze[50][50][50];//保存立方信息 
struct N{
	//状态结构体
	int x,y,z;
	int t; 
};
queue<N> Q;//队列，队列中的元素为状态
int go[][3]={
1,0,0,-1,0,0,0,1,0,0,-1,0,0,0,1,0,0,-1};
int BFS(int a ,int b,int c){
	//广度优先搜索，返回最小耗费时间
	while(Q.empty()==false){
		N now=Q.front();//得到队头的状态
		Q.pop();//从队列中弹出队头状态
		for(int i=0;i<6;i++){
			int nx=now.x+go[i][0];
			int ny=now.y+go[i][1];
			int nz=now.z+go[i][2];//计算新坐标 
			if(nx<0||nx>=a||ny<0||ny>=b|nz<0||nz>=c) continue;
			if(maze[nx][ny][nz]==1) continue;
			if(mark[nx][ny][nz]==true) continue;
			N tmp;
			tmp.x=nx;
			tmp.y=ny;
			tmp.z=nz;
			tmp.t=now.t+1;
			Q.push(tmp);
			mark[nx][ny][nz]=true;//标记该坐标
			if(nx==a-1&ny==b-1&&nz==c-1) return tmp.t;// 该坐标就是终点。可以直接返回其耗时
			 
		} 
	} 
	return -1; 
} 
int main(){
	int T;
	scanf("%d",&T);
	while(T--){
		int a,b,c,t;
		scanf("%d%d%d%d",&a,&b,&c,&t);//输入
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				for(int k=0;k<c;k++){
					scanf("%d",&maze[i][j][k]);//输入立方体信息
					mark[i][j][k]=false;//初始化标记数组 
				}
			}
		} 
		while(Q.empty()==false) Q.pop();//清空队列
		mark[0][0][0]=true;//标记起点
		N tmp;
		tmp.t=tmp.x=tmp.y=tmp.z=0;//初始状态
		Q.push(tmp);//将初始状态放入队列
		int rec=BFS(a,b,c);//广度优先搜索 
		if(rec<=t) printf("%d\n",rec);//若所需符合条件，输出
		else printf("-1\n"); 
	} 
	return 0;
	
} 

#include<stdio.h>
#include<vector>
#include<queue>
using namespace std;
vector<int> edge[501] //领结链表，只保存节点编号 
queue<int> Q
int main(){
	int inDegree[501];//统计每个节点的入度
	int n,m;//节点和边的个数 
	while(scanf("%d%d",&n,&m)!=EOF){
		if(n==0&&m==0 )   break;
		for(int i=0;i<n;i++){
			inDegree[i]=0;//初始化入度信息，所有节点入度均为0
			edge[i].clear();//清空邻接链表 
		}
		while(m--){
			int a,b;
			scanf("%d%d",&a,&b);//a指向b 
			iDegree[b]++;
			edge[a].push_back(b);//将b加入a的领结链表 
		} 
		while(Q.empty()==false) Q.pop();//清空队列
		for(int i=0;i<n;i++){
			if(inDegree[i]==0) Q.push(i);//节点入度为0，则放入队列 
		} 
		int cnt=0;//计数器。，累加已经加入拓扑序列的个数
		while(Q.empty()=false){//取出队头为0的节点 
			int nowp=Q.front();
			Q.pop();
			cnt++;
			for(int i=0;i<edge[nowP].size();i++){
				inDegree[edge[nowP][i]]--;//去除某条边，改边所指的后继节点-1
				if(inDegree[edge[nowP][i]]==0){
					Q.push(edge[nowP][i]);//将入度为0的放入队列，重复 
				} 
			} 
			
		} 
		 if(cnt==n) puts("YES");
		 else puts("no");
		  
		
	} 
	return 0;
	
} 

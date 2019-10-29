#include<stdio.h>
#include<vector>
#include<queue>
using namespace std;
vector<int> edge[501] //�������ֻ����ڵ��� 
queue<int> Q
int main(){
	int inDegree[501];//ͳ��ÿ���ڵ�����
	int n,m;//�ڵ�ͱߵĸ��� 
	while(scanf("%d%d",&n,&m)!=EOF){
		if(n==0&&m==0 )   break;
		for(int i=0;i<n;i++){
			inDegree[i]=0;//��ʼ�������Ϣ�����нڵ���Ⱦ�Ϊ0
			edge[i].clear();//����ڽ����� 
		}
		while(m--){
			int a,b;
			scanf("%d%d",&a,&b);//aָ��b 
			iDegree[b]++;
			edge[a].push_back(b);//��b����a��������� 
		} 
		while(Q.empty()==false) Q.pop();//��ն���
		for(int i=0;i<n;i++){
			if(inDegree[i]==0) Q.push(i);//�ڵ����Ϊ0���������� 
		} 
		int cnt=0;//�����������ۼ��Ѿ������������еĸ���
		while(Q.empty()=false){//ȡ����ͷΪ0�Ľڵ� 
			int nowp=Q.front();
			Q.pop();
			cnt++;
			for(int i=0;i<edge[nowP].size();i++){
				inDegree[edge[nowP][i]]--;//ȥ��ĳ���ߣ��ı���ָ�ĺ�̽ڵ�-1
				if(inDegree[edge[nowP][i]]==0){
					Q.push(edge[nowP][i]);//�����Ϊ0�ķ�����У��ظ� 
				} 
			} 
			
		} 
		 if(cnt==n) puts("YES");
		 else puts("no");
		  
		
	} 
	return 0;
	
} 

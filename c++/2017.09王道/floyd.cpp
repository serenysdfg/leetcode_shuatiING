#include<stdio.h>

int ans[101][101];

int main(){
	int n,m;
	while((scanf("%d%d",&m,&n))!=EOF){
		if(n==0&&m==0) break;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				ans[i][j]=-1;//����Ӿ�����С�� 
			}
			 ans[i][i]=0;//�Լ����Լ�ΰ0 
		}
	   
	
	
	while(m--){
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		ans[a][b]=ans[b][a]=c;//���ڽӾ���ֵ������������ͼ���ø�ֵҪ�������� 
	} 
	for(int k=1;k<n;k++){
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(ans[i][k]==-1||ans[k][j]==-1) continue; //����ֵ�в���ͨ��k���� 
				if(ans[i][j]==-1||ans[i][k]+ans[k][j]<ans[i][j]) ans[i][j]=ans[i][k]+ans[k][j];
			}
			
		}
	} 
	printf("%d\n",ans[1][n]);//ѭ������������� 
	return 0; 
	}
}

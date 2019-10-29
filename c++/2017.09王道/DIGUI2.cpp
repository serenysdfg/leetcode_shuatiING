#include<stdio.h>
#include<string.h>
int ans[22];
bool hash[22];//���֮ǰ�����뻷���� 
int n;
int prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41};
bool judge(int x){  //�ж�һ�����Ƿ�Ϊ���� 
	for(int i=0;i<13;i++){
		if(prime[i]==x) return true;
	}
	return false;
}

void check(){ //�������ɻ��ݷ�ö�ٵõ��Ľ� 
	if(judge(ans[n]+ans[1])==false) return;
	for(int i=1;i<=n;i++){
		if(i!=1) printf(" ");
		printf("%d",ans[i]);
	}
	printf("\n");
}


void DFS(int num){
	if(num>1) {
		if(judge(ans[num]+ans[num-1])==false) return ;
	} 
	if(num==n){
		check();
		return;
	}
	for(int i=2;i<=n;i++){
		if(hash[i]==false){
			hash[i]=true;
			ans[num+1]=i;
			DFS(num+1);
			hash[i]=false;
		}
	}
}

int main(){
	int cas=0;
	while(scanf("%d",&n)!=EOF){
		cas++;//case������
		for(int i=0;i<22;i++){
			hash[i]=false;//���δ��ʹ�� 
		} 
		ans[1]=1;
		printf("Case %d:\n",cas) ;
		hash[1]=true;
		DFS(1);//����������һ�������֣���1
		printf("\n") ;
	}
	return 0;
}

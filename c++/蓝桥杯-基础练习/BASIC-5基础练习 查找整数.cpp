/*
��������
����һ������n�����������У�������a�������еĵ�һ�γ����ǵڼ�����
���a�������г����ˣ��������һ�γ��ֵ�λ��(λ�ô�1��ʼ���)���������-1��
��������
6
1 9 4 8 3 9
9
�������
2
*/
#include<iostream>
using namespace std;
int main(){
	const int MAXN=10001;
	int n,a[MAXN],f,ans=-1;//,ans=-1��ǰ���� 
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	} 
	cin>>f;

	for(int i=0;i<n;i++){
		if(f==a[i]){
			ans=i+1;
		
		}
	}
	cout<<ans;
	return 0;
}

/*��������
����n�������ҳ���n���������ֵ����Сֵ���͡�
�����ʽ
��һ��Ϊ����n����ʾ���ĸ�����
�ڶ�����n������Ϊ������n������ÿ�����ľ���ֵ��С��10000��???
�����ʽ
������У�ÿ��һ����������һ�����ֵ���ڶ��б���Сֵ�������б�ʾ��Щ���ĺ͡�
*/
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int main(){
    int n;
    while(cin>>n){
        int a[10005];
        int sum=0;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        sort(a,a+n);//�����С���� 
        cout<<a[n-1]<<endl<<a[0]<<endl<<sum<<endl;
    }
    return 0;
}
/*
#include<iostream>
using namespace std;
int main(){
	const int MAXN=10001;
	int n,a[MAXN],max,min,sum=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
		sum+=a[i];
	} 
	for(int i=0;i<n-1;i++){
		if(a[i+1]<a[i]){
			int temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;		
		}
	}
	max=a[n-1];
	for(int i=n-1;i>0;i--){
		if(a[i-1]>a[i]){
			int temp=a[i];
			a[i]=a[i-1];
			a[i-1]=temp;		
		}
	}
	min=a[0];
	cout<<max<endl<<min<<endl <<sum<<endl;
	return 0;
} 
*/

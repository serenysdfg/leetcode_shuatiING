#include<iostream>
#include<algorithm> 

using namespace std;
int a[8],b[8];
int main()
{
	int T,n;
	int i,j;
	cin>>T;
	while(T--)
	{
		int sum=0;
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++)
		{
			sum+=a[i]*b[n-1-i];
		}
		cout<<sum<<endl;
	}
	return 0;
}


/*
#include<stdio.h>

void sort1(int *a,int n) //冒泡从小到大 
{
	int i,j;
	int tmp;
	for(i=0;i<n-1;i++)
		for(j=0;j<n-1-i;j++)
			if(a[j]>a[j+1])
			{
				tmp=a[j];
				a[j]=a[j+1];
				a[j+1]=tmp;
			}
}
void sort2(int *a,int n)//冒泡从大到小
{
	int i,j;
	int tmp;
	for(i=0;i<n-1;i++)
		for(j=0;j<n-1-i;j++)
			if(a[j]<a[j+1])
			{
				tmp=a[j];
				a[j]=a[j+1];
				a[j+1]=tmp;
			}
}
int main(void)
{
	int T;
	int n,i;
	int total;
	int a[8],b[8],c[8];
	scanf("%d",&T);
	while(T)
	{
		total=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort1(a,n);
		sort2(b,n);
		
		for(i=0;i<n;i++)
			c[i]=a[i]*b[i];
		for(i=0;i<n;i++)
			total+=c[i];
		printf("%d\n",total);
		T--;
	}
	return 0;
}


*/


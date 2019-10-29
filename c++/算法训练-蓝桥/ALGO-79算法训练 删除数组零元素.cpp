#include "stdio.h"

int CompactIntegers(int a[], int len)  //重要，数组前移。。 
{
    int i, j, k;
    for(k=0; k<len; k++)
    for(i=0; i<len; i++)
    {
        if(a[i] == 0)
        {
                for(j=i; j<len-1; j++)
                    a[j] = a[j+1];
                len--;
        }
    }
    return len;
}
void print(int a[], int len)
{
    int i;
    for(i=0; i<len; i++)
        printf("%d ", a[i]);
    printf("\n");
}
int main()
{
    int a[100000];
    int n;
    scanf("%d", &n);  
    int i;
    for(i=0; i<n; i++)
        scanf("%d", &a[i]);
        
        
    int len = CompactIntegers(a, n);//函数 
    
    if(len>1)
    {
        printf("%d\n", len);
        print(a, len);
    }
    else
        printf("%d", 0);
    getchar();
    getchar();    
    getchar();

}

/*c++
#include<iostream>
#include<cstring>

using namespace std;
int main(){	
	int n;
	int *arr;
	cin>>n;
	arr = new int[n];	
	int num = 0;	
	for (int i=0; i<n; ++i)
	{
		cin>>arr[i];
		if(arr[i] != 0)
		{
			++num;
		}
	}
	cout<<num<<endl;
	for(int i=0;i<n;i++){
		if(arr[i]!=0){
			cout<<arr[i]<<" ";
		}
	}

}
*/

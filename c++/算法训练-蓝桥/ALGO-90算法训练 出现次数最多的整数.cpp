#include "iostream"
using namespace std;
int main()
{
	int n;
	cin>>n;
	if(n <= 0) return 0;
	string *a = new string[n];
	int i;
	for(i = 0; i < n; ++i)
		cin>>a[i];

	string number = a[0];
	int count = 1;
	int flag = 1;
	
	for(i = 1; i < n; ++i)
	{
		if(a[i].compare(a[i - 1]) == 0)//相等 
			flag = flag + 1;
		if(a[i].compare(a[i - 1]) == 0 || i == n -1)
		{
			if(flag > count)
			{
				count = flag;//出现次数 
				number = a[i - 1];
			}
			flag = 1;
		}
	}
	cout<<endl;
	cout<<number<<" "<<count<<endl;
	return 0;
}


#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int i,t;
	vector<int> v;
	for (i = 0; i < 10; i++)
	{	
		cin>>t;
		v.push_back(t);
	}
	sort(v.begin(),v.end());
	v.erase(unique(v.begin(),v.end()),v.end());//unique(n.begin(),n.end())；unique()把相邻元素重复的甩到后面//erase()用来删掉后面的重复元素.//一定要先排序，再使用unique()，
	for (i = 0; i < v.size(); i++)
		cout<<v[i]<<endl;
	return 0;
}


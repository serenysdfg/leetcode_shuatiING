#include <iostream>
#include <cmath>
#include <string>
#include <windows.h>
#include <stack>
#include <vector>
using namespace std;
int main(int argc, char** argv) {
	vector<int> cs;
	int n;
	cin >> n;
	cs.push_back(1);
	for (int i = 2; i <= n; i++)
	{
		for (int j = 0; j<cs.size(); j++)
		{
			cs[j] *= i;
		}
		for (int j = 0; j<cs.size() - 1; j++)
		{
			if (cs[j]>9)
			{
				cs[j + 1] += cs[j] / 10;
				cs[j] = cs[j] % 10;
			}
		}
		while (cs[cs.size() - 1]>9)
		{
			cs.push_back(cs[cs.size() - 1] / 10);
			cs[cs.size() - 2] = cs[cs.size() - 2] % 10;
		}
	}
	for (int i = 0; i < cs.size() ; i++)
	{
		if (cs[i]!=0)
		{
			cout << (char)(cs[i] + '0');
			break;
		}
	}
	return 0;
}


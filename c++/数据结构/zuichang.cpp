#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int max = 0,k;
    string s[5];
    for (int i = 0; i < 5; ++i)
    {
        cin >> s[i];
        if(s[i].size()>max)
        {
        	max=s[i].size();
        	k=i;
        }
    }
    cout<<s[k]<<endl;
    return 0;
}


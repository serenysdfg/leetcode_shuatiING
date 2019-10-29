#include <iostream>
#include <string>
using namespace std;
int main()
{
    string str;
    int n;
    cin>>str;
    unsigned i;//
    n=str.length();
    for(i=0;i<n;i++)
    {
        if(str[i]>='A'&&str[i]<='Z')
            str[i]+=32;
        else if(str[i]>='a'&&str[i]<='z')
            str[i]-=32;
    }
    cout<<str;
    return 0;
}


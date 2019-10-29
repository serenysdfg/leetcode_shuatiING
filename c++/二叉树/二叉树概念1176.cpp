
#include <iostream>  
#include <math.h>  
using namespace std;  
  
const int N=1003;  
int a[N];  
  
int main()  
{  
    int n;  
    while(cin>>n)  
    {  
        for(int i=0;i<n;i++)  
            cin>>a[i];  
        int depth;  
        cin>>depth;  
        int start=(int)pow(2.0,depth-1);  
        bool flag=true;  
        for(int i=0;i<start&&start+i-1<n;i++)  
        {  
            if(flag)  
            {  
                flag=false;  
                cout<<a[start+i-1];  
            }  
            else  
                cout<<" "<<a[start+i-1];  
        }  
        cout<<endl;  
    }  
    return 0;  
}  

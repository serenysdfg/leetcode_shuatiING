#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

const int N = 1000;
const int INF = 999999;

int n,k, Max;
int stamp[20];
int MaxStamp[20];

void run( int step, int m, vector<int>);

void copy( int a[], int b[], int j )
{
    int i;
    for( i=1; i<=j; i++ )
        a[i]=b[i];
}

int min( int a, int b)
{
    return a>b?b:a;
}

int find(int v, vector<int> &den )
{
    int i;
    den[v]=1;
    for( i=1; i<=v*n; i++ )
    {

        if( den[i] < n  )
            den[v+i] = min( den[i]+1, den[v+i] );
    }

    for( i=1; i<=v*n; i++ )
        if( den[i] == INF )
            return i-1;

}




void dfs( int step, int m, vector<int> den )
{

    if( step > k )
    {
        if( m > Max )
        {
            copy(MaxStamp, stamp, k);
            Max=m;
        }
        return ;
    }

    run(step, m, den);
}

void run( int step, int m, vector<int> den)
{
    int i;
    for( i=m+1; i>stamp[step-1]; --i)
    {
        stamp[step]=i;
        vector<int> tden(den);
        int t= find(i, tden);

        //cout << "step: " << step << " " << stamp[step] <<endl;
        //cout << "  find: " << i << " " << t << endl;

        dfs(step+1, t, tden);
    }
}

int main()
{
    while( cin >> n >> k )
    {
        vector<int> den(N, INF);
        int i;
        stamp[1]=1;
        Max=n;
        for( i=1; i<=n; i++ )
            den[i]=i;

        dfs(2, n, den);

        for( i=1; i<k; i++ )
            cout << MaxStamp[i] << " ";
        cout << MaxStamp[i] << endl;

        cout << "MAX=" << Max << endl;
    }
    return 0;
}


include<iostream>
using namespace std;
int main(){
	int n,count,l1,l2;
	string s1,s2;
	cin>>n;
	int a[n];
	for(int k=0;k<n;k++){
		count=0;
		cin<<s1<<s2;
		l1=s1.size();
		l2=s2.size();
		for(int i=0;i<l2;i++){
			for(int j=0;j<l1;j++){
				if(s1[j]==s2[i]){
					i++;
					j++
					
				}
			}
		}
		
		a[i]=count;
	}
	for(int k=0;k<n;k++){
		cout<<a[k]<<endl; 
	} 
    
    return 0;
}

/*
#include<iostream>
#include<cstring>
using namespace std;
int Next[10000],ans=0;
void cal_next( string string, int len) //主串重复的记录  
{
	int i,pre=0;
	for ( i = 1;i < len;i++)
	{
		if (string[i] != string[pre])
			Next[i] =pre=0;
		else
			Next[i] = ++pre;
	}
}
void KMP(string string1,string string2, int len1, int len2)
{
	int i=0, j=0;
	while( i < len1)
	{
		for (;j < len2;j++)
			if (string1[i + j]!= string2[j])
				break;
		if (j == len2)  ans++;
		if(j!=0)
		i = i +j-Next[j-1],j = Next[j - 1];
		else i++;
	}
}
int main()
{
	string a, b;
	int N;
	cin >> N;
	while (N--) {
		ans = 0;
		memset(Next, 0, sizeof(Next));
		cin >> a >> b;
		int len1 = a.size(), len2 = b.size();
		cal_next(a, len1);
		KMP(b, a, len2, len1);
		cout << ans << endl;
	}
	return 0;
} 
*/

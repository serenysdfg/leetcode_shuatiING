#include <iostream>
#include <map>

/*
#include <cmath>
#include <string>
#include <windows.h>
#include <stack>
#include <vector>
#include <iomanip> 
#include <stack> 
#include <set>*/
using namespace std;
char GetCapital(char c)
{
	if(c<='Z')
		return c;
	else
		return c-('a'-'A');	//大写转换 
}
int main(int argc, char** argv) {
	map<char,int> a,b; //键值对容器 
	string t;
	cin>>t;
	for(int i=0;i<t.length();i++) // 
		a[GetCapital(t[i])]++;
	cin>>t;
	for(int i=0;i<t.length();i++)
		b[GetCapital(t[i])]++;  //a[65]是A ，数组完全相同 
	if(a==b){
		cout<<"Y";}
	else
		cout<<"N";
	return 0;
}


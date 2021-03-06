
#include<iostream>
#include<cstring>
using namespace std;

struct tstudent
{
	char name[21];
	char num[21];
	char sex;
};

void readdata(tstudent student[], int n)
{
	//输入N个学生的信息
	int i;
	for(i=0;i<n;i++)
	{
		cin>>student[i].name>>student[i].num>>student[i].sex;
	}
}

int findstudent(tstudent student[], int n, char* data)
{
	if (data == NULL)
		return -1;
	//判断是否有某个学生的学号或名字等于data，如果有，函数返回该学生在student数组中的序号，否则返回-1
	int i;
	for(i=0;i<n;i++)
	{
		if(strcmp(student[i].name,data)==0 || strcmp(student[i].num,data)==0){
		//	cout<<student[i].name<<"\t"<<student[i].num<<"\t"<<student[i].sex<<"\t"<<data<<"\t"<<strcmp(student[i].name,data)<<"\t"<<strcmp(student[i].num,data)<<endl;
			return i;
		}
	}
	return -1;
}
	
void solve(tstudent student[], int n, int m)
{
	char x[21], y[21];
	for (int i=0; i<m; i++) {
		//输入两个人的信息X、Y。通过调用findstudent函数判断这两个人能否成为舞伴
		cin>>x>>y;
		int a = findstudent(student,n,x);
		int b = findstudent(student,n,y);
		
		if(student[a].sex == student[b].sex)
			cout<<"N"<<endl;
		else
			cout<<"Y"<<endl;
	}
}

int main(void)
{
	int n, m;
	tstudent student[1010];	
	cin>>n;	
	readdata(student, n);
	cin>>m;
	solve(student, n, m);
	return 0; 
}


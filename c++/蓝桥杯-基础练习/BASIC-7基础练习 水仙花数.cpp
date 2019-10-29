#include<iostream>
using namespace std;
int main(){
	for(int a=1;a<10;a++){
		for(int b=0;b<10;b++){
			for(int c=0;c<10;c++){
				if(a*100+b*10+c==a*a*a+b*b*b+c*c*c){
					cout<<a*100+b*10+c<<endl;
				}
			}
		}
	}
	
	return 0;
} 
/*
#include<iostream>
using namespace std;
int main()
{
    int i,j,k;
    for(i=1;i<=9;i++)
    {
        for(j=0;j<=9;j++)
        {
            for(k=0;k<=9;k++)
            {
                if(i*100+j*10+k==i*i*i+j*j*j+k*k*k)
                {
                    cout<<i*100+j*10+k<<endl;
                }
            }
        }
    }
    return 0;
}

*/

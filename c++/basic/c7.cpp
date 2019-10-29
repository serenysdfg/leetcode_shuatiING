#include<iostream>
#include<cstdlib> 
#include<cstring>
using namespace std;
class Complex{
private:
 double r,i;
public:
 void print(){
  cout<<r<<"+"<<i<<"i"<<endl;
 }
 Complex& operator=(char s[])
 {
     int i;
     int len=sizeof(s)/sizeof(s[0]);
     for(i=0;i<len;i++)
     {
         char* c=new char[len+1];
         while(s[i]!='+'&&s[i]!='i')
         {
             c[i]=s[i];
             i++;
         }
         if(s[i]=='i')
         {
             this->i=atof(c); break;
         }
         else if(s[i]=='+')
         {
             r=atof(c);
             strcpy(c,s+i+1);
             this->i=atof(c);
         }
         return *this;
     }
 }
};
int main(){
 Complex a;
 a="3+4i";a.print();
 a="5+6i";a.print();
 return 0;
}

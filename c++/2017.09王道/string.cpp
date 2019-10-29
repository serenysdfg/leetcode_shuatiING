#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main(){
	string s;
	char c;
	int l;
	while(cin>>s){
		cin>>c;
		l=s.size();
		for(int i=0;i<l;i++){
			if(s[i]==c){
				cout<<"";
			}
			else{
				cout<<s[i];
			}
			
		}
		cout<<endl;
	}



	return 0;
}

/*
ÑùÀýÊäÈë£º
    You want someone to help you
    You
    I
ÑùÀýÊä³ö£º
    I want someone to help you

*/ 
#include<iostream>
/*
#include<cstring>
#include<cstdio>
using namespace std;
int main(){
	int j;
	char s1[100][100],s2[100],s3[100];
	while(scanf("%s",s1[0])!=EOF){
		int i=1;
		while(getchar()!='\n'){
			scanf("%s",s1[i++]);
		}
		scanf("%s",s2);
		scanf("%s",s3);		
		for(j=0;j<i-1;j++){
			if(strcmp(s1[j],s2)==0){
				printf("%s ",s3);//Ìæ»» ,Ó´¿Õ¸ñ 
			}
			else{
				printf("%s ",s1[j]); 
			}
	
		}
		if(strcmp(s1[j],s2)==0)  
            printf("%s\n",s3);  
        else  
            printf("%s\n",s1[j]);  
	}
	return 0;
}

*/
	     
   

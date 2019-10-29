#include<cstdio>

int main(){
	int v1,v2,l1=0,l2=0,l,t,s,ans=0;
	scanf("%d%d%d%d%d",&v1,&v2,&t,&s,&l);
	while(1){
		if(l1-l2>=t&&l1<l&&l2<l){  // >=拫實變+數奀 
			for(int i=1;i<=s;i++){ // i=1;
				l2+=v2;
				ans++;
			}
		}
		else{   //珨れ變 
			l1+=v1;
			l2+=v2;
			ans++;
		}
		if(l1>=l)break;  //礿砦 
		if(l2>=l)break;
	}
  	 if(l1>=l&&l2>=l){printf("D\n%d\n",ans);return 0;}
     if(l1>=l) {printf("R\n%d\n",ans); return 0;}
     if(l2>=l) {printf("T\n%d\n",ans); return 0;}
     return 0;
	
}
/*

#include<cstdio>
 #include<iostream>
 using namespace std;
 int main()
 {
     int v1,v2,t,s,L,L1=0,L2=0,ans=0,i,j;
     bool bk=true;
     scanf("%d%d%d%d%d",&v1,&v2,&t,&s,&L);
     while(1)
     {
         if(L1-L2>=t&&L1<L&&L2<L)
         {
            for(i=1;i<=s;i++)
            {
               if(L1<L&&L2<L)
               {
              L2+=v2;
              ans++;
               }
            }
         }
         else
         {
             L2+=v2;
             L1+=v1;
             ans++;
         }
         if(L1>=L) break;
         if(L2>=L) break;
     }
     if(L1>=L&&L2>=L){printf("D\n%d\n",ans);return 0;}
     if(L1>=L) {printf("R\n%d\n",ans); return 0;}
     if(L2>=L) {printf("T\n%d\n",ans); return 0;}
     return 0;
 }
 */

#include<sdtio.h
#include<stdlib.h>
bool isPrime(int num){
	if(1==num) return false;
	for(int i=2;i*i<=num;i++){
		if(0==num%i)
		return false;
	} 
	return true;
}

int main(){
	int n,count ,num;
	scanf("%d",&n);
	while(n--){
		int sum=0;
		scanf("%d",&count);
		while(count--){
			scanf("%d",&num);
			if(isPrime(num))sum+=num;
		}
		
	}
	return 0;
}


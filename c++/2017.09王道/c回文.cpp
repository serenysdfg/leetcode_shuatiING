//123321是一个非常特殊的数，它从左边读和从右边读是一样的。
//输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
 #include<stdio.h>
 int main(){
 	int a,b,c,d,e,f,t,all;
 	scanf("%d",&t);
 	for(a=1;a<10;a++){
 		for(b=0;b<10;b++)
 			for(c=0;c<10;c++)
 				for(d=0;d<10;d++)
 					for(e=0;e<10;e++){
 						if(a==e)
 							if(b==d){
 								all=a+b+c+d+e;
								if(all=t)
								printf("%d\n",a*10000+b*1000+c*100+d*10+e);
 							}
 					}
 	 for(a=1;a<10;a++)
	  	for(b=0;b<10;b++)
		  	for(c=0;c<10;c++)
			  	for(d=0;d<10;d++)
				  	for(e=0;e<10;e++)
					  	for(f=0;f<10;f++)
						  {
						  	if(a==f)
						  	 	if(b==e)
						  	 		if(c==d){
						  	 			all=a+b+c+d+e+f;
						  	 			if(all=t)
						  	 			printf("%d\n",a*100000+b*10000+c*1000+d*100+e*10+f);
						  	 		}
						  	
						  } 
						return 0;
 	}
 }

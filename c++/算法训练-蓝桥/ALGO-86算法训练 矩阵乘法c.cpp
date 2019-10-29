# include<stdio.h>
int main(){
	int m,s,n,i,j,k,a[200][200],b[200][200],c[200][200];
	scanf("%d%d%d",&m,&s,&n);
	for(i=1;i<=m;i++){
		for(j=1;j<=s;j++)
			scanf("%d",&a[i][j]);
	}
	for(i=1;i<=s;i++){
		for(j=1;j<=n;j++)
			scanf("%d",&b[i][j]);
	}
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++)
			c[i][j]=0;
	}
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++){
			for(k=1;k<=s;k++){
				c[i][j]=+=a[i][k]*b[k][j];
			}
		}
	}
	for(i=1;i<=m;i++){
		for(j=1;j<=n;j++)
			printf("%d ",c[i][j]);
		printf("\n");
	}
	return 0;
}


#include<cstdio>
#include<cstring>
int main()
{
	char s[65],str[65];
	int max=0,t,n,len;
	scanf("%d%s",&n,s);
	len=strlen(s);
	if(n <=len)
	{
		char ss[65],tt[65];
		for(int i=len;i>=n;i--)
		{
			ss[i]=tt[i]='\0';
			for(int j=0;j<=len-i;j++)
			{
				t=1;
				for(int k=0;k<i;k++)
				    ss[k]=s[k+j];
				for(int x=j+1;x<=len-i;x++)
				{
					for(int y=0;y<i;y++)
					    tt[y]=s[y+x];
					if(strcmp(ss,tt)==0)
					   t++;    
				}
				if(t>max)
		        {
			       max=t;
			       strcpy(str,ss);
//			       printf("%s\n",str);
		        }    
			}
		}

		printf("%s\n",str);
	}
}


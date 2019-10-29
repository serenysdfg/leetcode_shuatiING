#include <stdio.h>
int main()
{
	int i;
	char ch[100];
	gets(ch);
	i=0;
	while(ch[i]!='\0')
	{
		if(ch[i]<='z'&&ch[i]>='a')
			ch[i]-=32;
		else ch[i]+=32;
		i++;
	}
	puts(ch);

	return 0;
}



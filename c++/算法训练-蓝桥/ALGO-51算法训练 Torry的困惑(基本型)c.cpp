#include<stdio.h>
#include<math.h>
int pr[100010];
int top;

int isPrime(int n)
{
	int i;
	for(i = 0; i < sqrt(top); i++)
	{
		if(n % pr[i] == 0)
		{
			return 0;
		}
	}
	return 1;
}

int findNextPrime(void)
{
	int n = pr[top - 1] + 1;
	while(!isPrime(n))
	{
		n++;
	}
	pr[top++] = n;
	return n;
}

int main(void)
{
	int i, n;
	int result = 2;
	scanf("%d", &n);
	pr[0] = 2;
	top = 1;
	for(i = 1; i < n; i++)
	{
		int x = findNextPrime();
		result *= x;
		result %= 50000;
	}
	printf("%d", result);
	return 0;
}


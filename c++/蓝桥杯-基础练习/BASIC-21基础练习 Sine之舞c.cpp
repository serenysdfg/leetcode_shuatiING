#include <stdio.h>

void printA(int n, int k)
{
    if (n == k)
        printf("sin(%d)", n);
    else
    {
        printf("sin(%d", n);
        printf(n % 2 == 0 ? "+" : "-");
        printA(n + 1, k);
        printf(")");
    }
}

void printS(int n, int k)
{
    if (n == 1)
    {
        printA(1, n);
        printf("+%d", k - n);
    }
    else
    {
        printf("(");
        printS(n - 1, k);
        printf(")");
        printA(1, n);
        printf("+%d", k - n);
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    printS(N, N + 1);
    printf("\n");
    return 0;
}

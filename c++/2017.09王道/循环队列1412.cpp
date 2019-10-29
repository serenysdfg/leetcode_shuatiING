#include <stdio.h>
#include <string.h>

#define M 100000

int q[M+1], front, rear, m;

void init()
{
    front = rear = 0;
}

int Isempty()
{
    return (front == rear);
}

int Isfull()
{
    return (front == (rear+1)%m);
}

int push(int val)
{
    if (Isfull())
        return 0;
    q[rear] = val;
    rear = (rear+1)%m;
    return 1;
}

int pop(int *val)
{
    if (Isempty())
        return 0;
    *val = q[front];
    front = (front+1)%m;
    return 1;
}

int Query(int k, int *val)
{
    int count = (rear+m-front)%m;
    if (k <= 0 || k > count)
        return 0;
    *val = q[(front+k-1)%m];
    return 1;
}

int main(void)
{
    int n, i;
    char op[10];
    int k, val;

    while (scanf("%d%d", &n, &m) != EOF)
    {
        m ++;
        init();
        for(i=0; i<n; i++)
        {
            scanf("%s", op);
            if (strcmp(op, "Push") == 0)
            {
                scanf("%d", &k);
                if (! push(k))
                    printf("failed\n");
            }
            if (strcmp(op, "Pop") == 0)
            {
                if (! pop(&k))
                    printf("failed\n");
            }
            if (strcmp(op, "Query") == 0)
            {
                scanf("%d", &k);
                if (! Query(k, &val))
                    printf("failed\n");
                else
                    printf("%d\n", val);
            }
            if (strcmp(op, "Isempty") == 0)
            {
                if (! Isempty())
                    printf("no\n");
                else
                    printf("yes\n");
            }
            if (strcmp(op, "Isfull") == 0)
            {
                if (! Isfull())
                    printf("no\n");
                else
                    printf("yes\n");
            }
        }
    }

    return 0;
}       

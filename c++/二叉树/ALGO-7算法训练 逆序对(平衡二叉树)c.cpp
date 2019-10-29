#include<stdio.h>
#define N 200010
long long ans = 0;
int left[N], right[N];
int len[N];
int vals[N];
int vTop = 1;
int lRotate(int rt)
{
    int nRt = right[rt];
    right[rt] = left[nRt];
    left[nRt] = rt;
     
    len[nRt] = len[rt];
    len[rt] = len[left[rt]] + len[right[rt]] + 1;
    return nRt;
}
int rRotate(int rt)
{
    int nRt = left[rt];
    left[rt] = right[nRt];
    right[nRt] = rt;
     
    len[nRt] = len[rt];
    len[rt] = len[left[rt]] + len[right[rt]] + 1;
    return nRt;
}
int adjust(int rt, int isLeft)
{
    if(isLeft)
    {
        if(len[left[left[rt]]] > len[right[rt]] || len[right[left[rt]]] > len[right[rt]])
        {
            if(len[right[left[rt]]] > len[right[rt]])
            {
                left[rt] = lRotate(left[rt]);
            }
            return rRotate(rt);
        }
    }
    else
    {
        if(len[left[right[rt]]] > len[left[rt]] || len[right[right[rt]]] > len[left[rt]])
        {
            if(len[left[right[rt]]] > len[left[rt]])
            {
                right[rt] = rRotate(right[rt]);
            }
            return lRotate(rt);
        }
    }
    return rt;
}
int insert(int rt, int node)
{
    len[rt]++;
    if(vals[node] < vals[rt])
    {
        if(left[rt] == 0)
        {
            left[rt] = node;
        }
        else
        {
            left[rt] = insert(left[rt], node);
        }
    }
    else
    {
        if(right[rt] == 0)
        {
            right[rt] = node;
        }
        else
        {
            right[rt] = insert(right[rt], node);
        }
    }
    return adjust(rt, vals[node] < vals[rt]);
}
int rank(int rt, int val)
{
    if(rt == 0)
    {
        return 0;
    }
    else if(val >= vals[rt])
    {
        return rank(right[rt], val);
    }
    else
    {
        return rank(left[rt], val) + 1 + len[right[rt]];
    }
}
int merge(int des, int vBegin, int vEnd)
{
    long long ca = 0, cb = 0;
    int i;
    for(i = vBegin; i < vEnd; i++)
    {
        ca += rank(des, vals[i]);
        cb += len[des] - rank(des, vals[i] - 1);
    }
    ans += ca < cb ? ca : cb;
    for(i = vBegin; i < vEnd; i++)
    {
        left[i] = right[i] = 0;
        len[i] = 1;
        des = insert(des, i);
    }
    return des;
}
int buildTree()
{
    int val;
    scanf("%d", &val);
    if(val != 0)
    {
        left[vTop] = right[vTop] = 0;
        len[vTop] = 1;
        vals[vTop] = val;
        return vTop++;
    }
    int ls = vTop;
    int rlt = buildTree();
    int rs = vTop;
    int rrt = buildTree();
    int re = vTop;
    if(rs - ls > re - rs)
    {
        return merge(rlt, rs, re);
    }
    else
    {
        return merge(rrt, ls, rs);
    }
}
int main(void)
{
    int n;
    scanf("%d", &n);
    buildTree();
    printf("%I64d", ans);
    return 0;
}


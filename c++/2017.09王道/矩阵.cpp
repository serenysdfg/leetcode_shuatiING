#include <cstdio>
#include <algorithm>

struct Tree
{
    int sum, max;
};

Tree tree[1 << 18];

void scan(int &n)
{
    char c;
    
    c = getchar();
    if (c == EOF) {
        return ;
    }
    while (c < '0' || c > '9') {
        c = getchar();
    }
    n = c - '0';
    while (c = getchar(), c >= '0' && c <= '9') {
        n *= 10;
        n += c - '0';
    }
}

void put(int n)
{
    int cnt = 0;
    char s[16];
    
    if (n == 0) {
        putchar('0');
        return ;
    }
    for( ; n; n /= 10) {
        s[cnt++] = n % 10 + '0';
    }
    while (cnt--) {
        putchar(s[cnt]);
    }
}

void update(int n, int v)
{
    for (n += (1 << 17),tree[n].sum = tree[n].max = v, n >>= 1; n; n >>= 1) {
        tree[n].max = std::max(tree[n + n].max, tree[n + n + 1].max);
        tree[n].sum = tree[n + n].sum + tree[n + n + 1].sum;
    }
}

int query(int s, int t, int func)
{
    int sum = 0, max = 0;
    
    for (s += (1 << 17) - 1, t += (1 << 17) + 1; s ^ t ^ 1; s >>= 1, t >>= 1) {
        if (~s & 1) {
            sum += tree[s ^ 1].sum;
            max = std::max(max, tree[s ^ 1].max);
        }
        if (t & 1) {
            sum += tree[t ^ 1].sum;
            max = std::max(max, tree[t ^ 1].max);
        }
    }
    return func ? max : sum;
}

int main()
{
    int n, m, i, a, b, c;
    
    scan(n);scan(m);
    for (i = 1; i <= n; ++i) {
        scan(a);
        update(i, a);
    }
    while (m--) {
        scan(c);scan(a);scan(b);
        c == 1 && (update(a, b), 0);
        c == 2 && (put(query(a, b, 0)), putchar('\n'), 0);
        c == 3 && (put(query(a, b, 1)), putchar('\n'), 0);
    }
    return 0;
}

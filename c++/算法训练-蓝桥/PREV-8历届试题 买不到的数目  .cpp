#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 1000005;
int dp[maxn];

int main() {
	int n, m;
	while(scanf("%d %d", &n, &m) != EOF) {
		memset(dp, 0, sizeof(dp));
		dp[n] = 1, dp[m] = 1;
		int t = max(n, m);
		for(int i = t + 1; i < maxn; i++) {
			if(dp[i - n] || dp[i - m]) dp[i] = 1;
		}
		
		for(int i = maxn - 1; i >= 0; i--) {
			if(!dp[i]) {
				printf("%d\n", i);
				break;
			}
		}
	}
	return 0;
}






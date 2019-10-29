/*
 * @lc app=leetcode.cn id=231 lang=c
 *
 * [231] 2的幂
 *
 * https://leetcode-cn.com/problems/power-of-two/description/
 *
 * algorithms
 * Easy (44.02%)
 * Total Accepted:    11.9K
 * Total Submissions: 27.1K
 * Testcase Example:  '1'
 *
 * 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
 * 
 * 示例 1:
 * 
 * 输入: 1
 * 输出: true
 * 解释: 20 = 1
 * 
 * 示例 2:
 * 
 * 输入: 16
 * 输出: true
 * 解释: 24 = 16
 * 
 * 示例 3:
 * 
 * 输入: 218
 * 输出: false
 * 
 */
//  2的次方数都只有一个 1 ，剩下的都是 0 。根据这个特点，只需要每次判断最低位是否为 1(n & 1) ，然后向右移位(然后向右移位)，最后统计 1 的个数即可判断是否是 2 的次方数。

//2还有一种巧妙的解法。再观察上面的表格，如果一个数是 2 的次方数的话，那么它的二进数必然是最高位为1，其它都为 0 ，那么如果此时我们减 1 的话，则最高位会降一位，其余为 0 的位现在都为变为 1，那么我们把两数相与，就会得到 0
//一行代码搞定：return (n > 0) && (!(n & (n - 1)));
bool isPowerOfTwo(int n) {
    
    int cnt = 0;
    while (n > 0) {
        cnt += (n & 1);
        n >>= 1;
    }
    return cnt == 1;
    
    
}


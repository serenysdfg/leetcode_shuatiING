// 滑动窗口问题 - 双指针法
//  双指针，动态维护一个区间。尾指针不断往后扫，当扫到有一个窗口包含了所有T 的字符后，
//  然后再收缩头指针，直到不能再收缩为止。最后记录所有可能的情况中窗口最小的 public class Solution
// {
  public
    String minWindow(String S, String T)
    {
        int[] srcHash = new int[255]; //srcHash目标字符串
        // 记录目标字符串每个字母出现次数
        for (int i = 0; i < T.length(); i++)
        {
            srcHash[T.charAt(i)]++;
        }
        int start = 0, i = 0;
        // 用于记录窗口内每个字母出现次数
        int[] destHash = new int[255];
        int found = 0;                                            //找到的一个匹配字符
        int begin = -1, end = S.length(), minLength = S.length(); //minLength最短窗口
        for (start = i = 0; i < S.length(); i++)
        {
            destHash[S.charAt(i)]++; // 每来一个字符给它的出现次数加1
            if (destHash[S.charAt(i)] <= srcHash[S.charAt(i)])
                found++; // 如果加1后这个字符的数量不超过目标串中该字符的数量，则找到了一个匹配字符
            // 如果找到的匹配字符数等于目标串长度，说明找到了一个符合要求的子串
            if (found == T.length())
            {
                // 将开头没用的都跳过，没用是指该字符出现次数超过了目标串中出现的次数，并把它们出现次数都减1，出现次数不能超过目标字符串
                while (start < i && destHash[S.charAt(start)] > srcHash[S.charAt(start)])
                {
                    destHash[S.charAt(start)]--;
                    start++;
                }
                // 这时候start指向该子串开头的字母，判断该子串长度
                if (i - start < minLength)
                {
                    minLength = i - start;
                    begin = start;
                    end = i;
                }
                // 把开头的这个匹配字符跳过，并将匹配字符数减1
                destHash[S.charAt(start)]--;
                found--;
                // 子串起始位置加1，我们开始看下一个子串了
                start++;
            }
        }
        // 如果begin没有修改过，返回空
        return begin == -1 ? "" : S.substring(begin, end + 1);
    }
}
/*
 * @lc app=leetcode id=20 lang=c
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (35.84%)
 * Total Accepted:    513.8K
 * Total Submissions: 1.4M
 * Testcase Example:  '"()"'
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * Note that an empty string is also considered valid.
 * 
 * Example 1:
 * 
 * 
 * Input: "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: "{[]}"
 * Output: true
 * 
 * 
 */
bool isValid(char* s) {
    stack<char> parentheses;
        for (char c:s) {
            if (!parentheses.empty()) {
                char first = parentheses.top(), second = c;
                if (first == '(') {
                    if (second == ')')
                        parentheses.pop();
                    else if (second == ']' || second == '}')
                        return false;
                    else
                        parentheses.push(second);
                } else if (first == '[') {
                    if (second == ']')
                        parentheses.pop();
                    else if (second == ')' || second == '}')
                        return false;
                    else
                        parentheses.push(second);
                } else if (first == '{') {
                    if (second == '}')
                        parentheses.pop();
                    else if (second == ')' || second == ']')
                        return false;
                    else
                        parentheses.push(second);
                }
            } else
                parentheses.push(c);
        }
        if(!parentheses.empty())
            return false;
        return true;
    }
};
    
}

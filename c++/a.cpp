字符
char[] a=new cahr[s.length()]
char ci=s.charAt(i)

private final static HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

链表
ListNode head：
listNode l1=head,l2=head.next;

回文
private boolean isPalindrome(String s,int i,int j){
	while(i<j){
		if(s.charAt(i++)!=s.charAt(j--)){
			return false;
		}
	}
	return true;
}

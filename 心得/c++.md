[TOC]

#### c++心得

 ###### 不要漏	c++
```
#include<iostream>
#include<malloc.h>
#include<stdio.h>
using namespace std;
```
c的头文件用于c++	#include<cstdio.h>

###### 栈

​	/*初始化顺序结构栈S*/
​	void InitStack(SeqStack *S){
​	

> 1. 	if(S->top<=0) return 1; #栈顶

###### 输入输出

###### ***\*输入\****

| c++输入 | string不用                         |
| ------- | ---------------------------------- |
|         | getline(cin,str1) ;/// cin>>s1>>s2 |
|         | str1.size();                       |
|         |                                    |
| c中？   | ***\*char str[21],\****            |
| 长度        | 能用strlen和gets                   |

***\*int len1 = a.size(), len2 = strlen(b.c_str());\**

getchar;//读取换行符

gets(str); 

尽量用scanf不要用gets**
int[] nums
nums.length;
pi	const double pi=acos(-1.0);
%f和%lf分别是float类型和double类型用于格式化输入输出时对应的格式符号。	
***\*定义\****	

```c++
private static Scanner scanner=new Scanner(System.in);	
​		private static String s1;	
​		public static void main(String[] args) {}	
```

​	***\*扫描输入文本的\****：s1=scanner.next();	
​		argc是命令行总的参数个数 	
​		argv[]是argc个参数，其中第0个参数是程序的全名，以后的参数	
***\*输出\****	>>用于cin对象,表示从标准输入,输入数据到变量中 <<用于cout对象,表示将变量数据,输出到标准输出中	

###### ***\*数组\****	
```c++
const int MAXN=40;	
​		int a[MAXN][MAXN];
```
***\*数组分配内\****存	

```c++
	int *arr;	
​	cin>>n;	
​	arr = new int[n];	
​	int a[10000>	
​	 scanf("%d", &a[i]);	
```
***\*数组参数\****	char *p	char a[]
```c++
			while(*p++!=0)
```
###### ***\*排序\****	
```c++
#include<algorithm>	
​		#include<cstring>	
​		 sort(a,a+n);//排序从小到大 	
​		while(cin>>n)	
```
sort(a+1,a+1+n,cmp);//默认从小到大 		
从大到小	bool cmp(int x,int y){ //x>y返回1 		
​		return x>y;	
***\*数组排序\****	
```c++
int cmp( const int &a, const int &b ){	
​	  if( a > b )	
​	    return 1;	
​	  else	
​	    return 0;	
​	}	
​	sort(a,a+n,cmp);	
```
​	是对数组a降序排序,从大带小cmp	

###### 其他
***\*高精度加法\**** 	:c[i+1]=c[i+1]+c[i]/10;	c[i]=c[i]%10;			
***\*筛法\****	筛法，求1万以内的所有素数	
***\*初始化\****	char s1[1000]={0},s2[1000]={0};  //初始化 	
​	scanf("%s%s",s1,s2);	
***\*字母转换\****	for(i=0;i<len;i++)	
​		if(a[i]>='a' && a[i]<='z') a[i]-=32;
***\*次数最多\****		if(a[i].compare(a[i - 1]) == 0)//相等 	
***\*矩阵\**** 	
     for(i=0;i<s;i++)	
​		for(j=0;j<n;j++)
​		   scanf("%d",&b[i][j]);

***\*字符串输\****入	arr = new int[n];	
###### ***\*求质数\****	***\*筛选法：\****
从小到大筛去一个已知素数的所有倍数。依次删除可被2整除，3整除。。。。的数字，剩下的则为素数 。	
开根号法：如果一个数（>2），对这个数求平方根，如果这个数能被这个数的平方根到2之间的任何一个（只要有一人就行）整除说明就不是质数，如果不能就说明是质数！	

***\*换行输出\****	 
for(int i=1;i<=n;i++)	
    for(int j=1;j<=m-1;j++)	
    printf("%d ",ans[i][j]);	
    printf("%d\n",ans[i][m]);	

***\*图关联矩阵\****	  
for(int i=1;i<=m;i++)		
​	    scanf("%d%d",&a,&b);		
​	    ans[a][i] = 1;		
​	    ans[b][i] = -1;		
***\*高位不断\*2\****	if(a[len-1]=='1')sum+=i;
​	i*=2;
​	len--;
***\*圈循环\****	s=(s+x)%i;
​	fabs:求浮点数x的绝对值
***\*小技巧\****
std::ios::sync_with_stdio(false);

***\*cin，cout之所以效率低\****：百 度了一下，原来而cin，cout之所以效率低，是因为先把要输出的东西存入缓冲区，再输出，导致效率降低，而这段语句可以来打消iostream的输入 输出缓存，可以节省许多时间，使效率与scanf与printf相差无几，还有应注意的是scanf与printf使用的头文件应是stdio.h而不是 iostream。

###### ***\*链表\****

```c++
newNode=(LinkList*)malloc(sizeof(LinkList));		
newNode->next=p; //插入新节点		
pre->next=newNode; 			
```

```c++
pre=head;		
p=head->next;		
//找到插入位置		
while(p){//一个个往后 		
​	if(newNode->data<p->data){	
​	    break;	}	
​	pre=p;	
​	p=p->next;	
}		
​	head=(LinkList*)malloc(sizeof(LinkList)); //***\*创建空链表\**** 	
​	head->next=NULL; 
```

***清屏***	clrscr，gotoxy，getch（），getche（）	
***防止溢出***	long long n
***时间***	printf("time used= %.2f\n",(double)clock()/CLOCKS_PER_SEC);
***输入字数不一定***	
while(scanf("%d",&x)==1){
​	enter然后ctrl+z，然后enter；；输入结束
while(readcodes())	
while(scanf(0)	

###### 文件	

freopen（“input.txt”,"r",stdin)
freopen（“output.txt”,"r",stdout)
###### 其他tip
***引号替换***
if(c == '"') { printf("%s", q ? "``" : "''"); q = !q; }
1使用fgetc(fin)可以从打开的文件fin中读取一个字符。一般情况下应当在检查它不是EOF后再将其转换成char值。从标准输入读取一个字符可以用getchar，它等价于fgetc(stdin)。
2 、C语言中的gets(s)存在缓冲区溢出漏洞，不推荐使用。在C11标准里，该函
数已被正式删除。
3、fgets(buf, maxn, fin)"将读取完整的一行放在字符数组buf中。应当保证buf足够存放下文件的一行内容。除了在文件结束前没有遇到“\n”这种特殊情况外，buf总是以“\n”结尾。当一个字符都没有读到时，fgets返回NULL。

###### ***\*读取有空格的字符串\****
```
	1	while(scanf("%s",s1[0]!=EOF)){		
​			while(getchar()!='\n'){	
​				scanf("%s",word[i++]);
​	2	char str[100];//有空格不能用cin ,用str的gets获取数组，转为string 		
​		gets(str);		
​		string a=str;	
```
#### 算法竞赛第三章
***对应镜像***：

新定义数组
​			if(s[i]!=s[len-1-i]) p=0;//不是回文串

​			if(r(s[i])!=s[len-1-i]) m=0;//不是镜像串

###### ***\*tip\****

头文件ctype.h中定义的isalpha、isdigit、isprint等工具可以用来判断字符的属性，而toupper、tolower等工具可以用来转换大小写。如果ch是大写字母，则ch-'A'就是它在字母表中的序号（A的序号是0，B的序号是1，依此类推）；类似地，如果ch是数字，则ch-'0'就是这个数字的数值本身


###### ***\*猜数字\****

```c++
int c1 = 0, c2 = 0; //统计数字d在答案序列和猜测序列中各出现多少次
for(int i = 0; i < n; i++) {
if(a[i] == d) c1++;
if(b[i] == d) c2++;
```


###### ***\*生成元\****

如果**x**加上**x**的各个数字之和得到**y**，就说**x**是**y**的生成元

```c++
for(int m = 1; m < maxn; m++) {
int x = m, y = m;
while(x > 0) { y += x % 10; x /= 10; }
if(ans[y] == 0 || m < ans[y]) ans[y] = m;
}
```

###### ***\*不断查询效率不高\****

：只需一次性枚举100000内的所有正整数**m**，标记“**m**加上**m**的各个数字之和得到的数有一个生成元是**m**”，***\*最后查表\****可。

###### ***\*环状序列\****

```c++
\#include<stdio.h>
\#include<string.h>
\#define maxn 105
```

//环状串s的表示法p是否比表示法q的字典序小

```c++
int less(const char* s, int p, int q) {
int n = strlen(s);
for(int i = 0; i < n; i++)
if(s[(p+i)%n] != s[(q+i)%n])
return s[(p+i)%n] < s[(q+i)%n];
return 0; //相等
```

```c++
int main() {
int T;
char s[maxn];
scanf("%d", &T);
while(T--) {
scanf("%s", s);
int ans = 0;
int n = strlen(s);
for(int i = 1; i < n; i++)
if(less(s, i, ans)) ans = i;
for(int i = 0; i < n; i++)
putchar(s[(i+ans)%n]);
putchar('\n');}}
return 0;}
```


###### ***\*提示\****

提示3-21：字符还可以直接用ASCII码表示。如果用八进制，应该写成：“\o”，“\oo”或“\ooo”（o为一个八进制数字）；如果用十六进制，应该写成“\xh”（h为十六进制数字串）。

数组的大小可以用sizeof在编译时获得（它不是一个函数），它经常被用在memset、memcpy

等函数中。有的函数并没有做大小检查，因而存在缓冲区溢出漏洞。本章中只讲了gets，但

其实strcpy也有类似问题——如果源字符串并不是以“\0”结尾的，复制工作将可能覆盖到缓冲区之外的内存。这也提醒我们：如果按照自己的方式处理字符串，千万要保证它以“\0结尾。

#### 第四章

```c++
string a="asdhuydfhuyhuyf";
string b="huy";
int start=0;
int pos=a.find(b,start);
a.insert(2,b);
erase
b[i]=tolower(b[i]);
```

##### ***\*//在b中删除a\****

//先查找位置

int pos=b.find(a,0);

while(pos!=-1){

##### 知识点：

***\*1、\*******\*自顶向下\*******\*：\****先写函数，伪代码，再写具体函数

2、标识符注意不用，全局变量少用

3、***\*1<** 1先转成二进制  在左移n位  然后补0，10的n次方

比如 1<<4 1的二进制为 0001 0000 左移4位 0001 0000. 如果再转成10进制就是16,左移n为也就是乘以[2的n次方](https://www.baidu.com/s?wd=2的n次方&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YLuhfYrHR3uWmYuAfzujcv0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EPj0kPWRsnWn3)

4、**\r** : return 到当前行的最左边。 \n: newline 向下移动一行,并不移动左右

5、scanf遇空格、“回车”、“跳格”键。就结束输入

###### ***\*6、\*******\*数组空间获取\****

int ans[maxn];

memset(ans, 0, sizeof(ans));

memcpy（d2,d,sizeof(d）),从d复制到d2，二维也可以

***\*7所有往前移动：\****

往前移，直接用=或者strcpy，循环

***8、头文件***
Time.h:clock
Ctype.h:isalpha,isdigit,toupper
***9、注意浮点误差***：+EPS：1e-6比如
***\*10、string区别c和c++：\****
C＋＋提供了一个新的string类型，用来替代***\*C语言中的字符数组\****。用户仍然可以继续用字符数组当字符串用，但是如果希望程序更加简单、自然，string类型往往是更好的选择。
例如，C＋＋的cin/cout可以直接读写string类型，却不能读写字符数组；string类型还可以像整数那样“相加”，而在***\*C语言里只能使用strcat函\****数。
C++：getlin
C：fgets
提示5-6：可以把string作为流进行读写，定义在sstream头文件中。
###### ***\*程序\****
刽子手：用left剩下需要猜的个数代替已经猜出的字母数组
##### ***\*跨行“读取字符的函数\****
```c++
int readchar(){ //”跨行“读取字符的函数 for(;; 
​	for(;;){
​		int ch=getchar();
​		if(ch!='\n'||ch!='\r') return ch;//一直读到非换行符为止，读到字符就输出 
​	}	
```
##### }***\*读取c位二进制数----转化为十进制\****
```c++
int readint(int c) { //读取c位二进制数----转化为十进制 不断读取*2
​	int v=0;
​	while(c--)	v=v*2+readchar()-'0';
​	return v;	
```

##### ***\*Execl读取思路\****
1、 模拟操作，所有单元格变换 或者操作保存对每个查询重新执行每个操作只需关注查询的单元格效率高
2、 思路：读取-记录
3、 一种方法，变化后寻找，另一种找一个，一步步变化 （好）

###### 算法竞赛第五章
###### ***\*1\*******\*、sort排序\****
sort可以对任意对象进行排序，不一定是内置类型。如果希望用sort排序，这个类型需要定义“小于”运算符，或者在排序时传入一个“小于”函数。排序对象可以存在于普通数组里，也可以存在于vector中（参见5.2.2节）。前者用sort（a，a＋n）的方式调用，后者用sort（v.begin( )，v.end( )）的方式调用。lower_bound的作用是查找“大于或者等于x的第一个位置”。

***\*提示5-11：\****algorithm头文件中的sort可以给任意对象排序，包括内置类型和自定义类型，前提是类型定义了“<”运算符。排序之后可以用lower_bound查找大于或等于x的第一个位置。待排序／查找的元素可以放在数组里，也可以放在vector里。还有一个unique函数可以删除有序数组中的重复元素，后面的例题中将展示其用法。

 

###### ***\*5.2.2　不定长数组：vector\****

vector就是一个不定长数组。不仅如此，它把一些常用操作“封装”在了vector类型内部。

例如，若a是一个vector，可以用a.size( )读取它的大小，a.resize( )改变大小，a.push_back( )向尾部添加元素，a.pop_back( )删除最后一个元素。

vector是一个模板类，所以需要用vector<int>a或者vector<double>b这样的方式来声明一

个vector。Vector<int>是一个类似于inta[]的整数数组，而vector<string>就是一个类似于

stringa[ ]的字符串数组。vector看上去像是“一等公民”，因为它们可以直接赋值，还可以作为函数的参数或者返回值，而无须像传递数组那样另外用一个变量指定元素个数

##### ***\*找到序号返回指针\****
```c++
void find_block(int a, int& p, int& h) {
 for(p = 0; p < n; p++)
  for(h = 0; h < pile[p].size(); h++)
   if(pile[p][h] == a) return;
}
```
```c++
## **1、** ***\*S\*******\*et\****
\#include<iostream>
\#include<string>
\#include<set>
\#include<sstream>
using namespace std;
set<string> dict;
string s, buf;
```

```c++
int main() {
 while(cin >> s) {
  for(int i = 0; i < s.length(); i++)
   			if(isalpha(s[i])) s[i] = tolower(s[i]); else s[i] = ' '; //转换为字母或者空格isalpha
  stringstream ss(s); //没看懂 
  while(ss >> buf) dict.insert(buf);//没看懂 
 }
 for(set<string>::iterator it = dict.begin(); it != dict.end(); ++it) //迭代器 
  cout << *it << "\n";
 return 0;
}
```
###### ***\*5\map\****

单词排序
```c++
\#include<iostream>
\#include<string>
\#include<cctype>
\#include<vector>
\#include<map>
\#include<algorithm>
using namespace std;

map<string,int> cnt;
vector<string> words;

// 将单词s标准化 ，重要 
string repr(string s) {
 string ans = s;
 for(int i = 0; i < ans.length(); i++)
  ans[i] = tolower(ans[i]);
 sort(ans.begin(), ans.end());
 return ans;
}}
```
```c++
int main() {
 int n = 0;
 string s;
 while(cin >> s) {
  if(s[0] == '#') break;
  words.push_back(s);
  string r = repr(s);
  if(!cnt.count(r)) cnt[r] = 0; //map的使用，先为0 
  cnt[r]++;
 }
 vector<string> ans;
 for(int i = 0; i < words.size(); i++)
  if(cnt[repr(words[i])] == 1) ans.push_back(words[i]);//获取不重复的 
 sort(ans.begin(), ans.end());
 for(int i = 0; i < ans.size(); i++)
  cout << ans[i] << "\n";
 return 0;
} 
```

# leetcode

### ***\*交换\****
```c++
private void swap(int[] a, int i, int j) {
  int t = a[i];
  a[i] = a[j];
  a[j] = t;
}
```
### ***\*排序\**** ***\*：\****

时间复杂度 O(NlogN)，空间复杂度 O(1)找到第 k 大的元素。
```c++
public int findKthLargest(int[] nums, int k) {
  Arrays.sort(nums);
  return nums[nums.length - k];
}
```
## ***\*算法\****
### ***\*贪心算法\****
最优装载，
1部分背包，乘船问题
2区间相关：选择不相交区间
3哈夫曼编码

## **1、** ***\*背包问题\****
http://blog.csdn.net/Return_True_hang/article/details/68952386
## ***\*0-1背包问题状态转移方程\****
用dp[i][j]表示前i个物品在总体积不超过j的情况下，放到背包里的最大价值。由此可以推出状态转移方程：
dp[0][j] = 0;
dp[i][j] = max{dp[i-1][j-v[i]] + w[i],dp[i-1][j]};
上面的式子应该很好理解，当第i物品的体积小于当前剩余的体积，则说明可以装入背包，那么dp[i][j] = dp[i-1][j-v[i]]+w[i]。反之就是不能转入背包，dp[i][j] = dp[i-1][j]。
```c++
		for(int i=1;i<=n;i++){
​			for(int j=s;j>=list[i].w;j--){
​				dp[i][j]=max(dp[i-1][j],dp[i-1][j-list[i].w]+list[i].v);		
​			} 
​			for(int j=list[i].w-1;j>=0;j--)
​				dp[i][j]=dp[i-1][j];}
​		printf("%d\n",dp[n][s]);//输出答案
```
###### ***\*1119\****

数位和相加
```c++
\#include<iostream>
using namespace std;
int main(){
​	int num1,num2,sum=0,a;
​	cin>>num1>>num2;
​	for (int i=num1;i<=num2;i++){
​		sum+=i/100+i%100/10+i%10;
​	}
​	cout<<sum;
}

 
​```c++
Opendir
=readdir(dir)
​	DIR *dir=opendir(folderPath);
​	struct dirent *i=NULL;

​	while((i=readdir(dir))!=NULL){
​		if(!strcmp(i->d_name,".")||!strcmp(i->d_name,".."))
​			continue;
```


c++中当定义类对象是指针对象时候，就需要用到 ***\*“->”\**** 指向类中的成员；当定义一般对象时候时就需要用到 ***\*“.”\**** 指向类中的成员…….
A *p则：p->play()使用; 左边是结构指针。 
A p 则：p.paly()使用; 左边是结构变量。

总结： 
***\*箭头（->）：左边必须为指针；\**** 
***\*点号（.）：左边必须为实体。\****

***\*1排序算法sort：\*******\*#include\****
int sushu(int num){ //判断是否为素数
for(int i = 2;i<=sqrt(num);i++){ 
if(num%i==0) return 0;
}

### ***\*文件读取\****
d_type
d_name


***\*5. 最后，总结一下，想要获取某目录下（比如a目下）b文件的详细信息，我们应该怎样做\****

首先，我们使用opendir函数打开目录a，返回指向目录a的DIR结构体c。
接着，我们调用readdir( c)函数读取目录a下所有文件（包括目录），返回指向目录a下所有文件的dirent结构体d。
然后，我们遍历d，调用stat（d->name,stat *e）来获取每个文件的详细信息，存储在stat结构体e中。
总体就是这样一种逐步细化的过程，在这一过程中，三种结构体扮演着不同的角
***\*S_ISREG(st_mode)\****：是否是一个常规文件.
***\*S_ISDIR(st_mode)\****：是否是一个目录

***\*truct stat\**** {
dev_t st_dev;
ino_t st_ino;
***\*mode_t st_mode;\****
```c++
***\*static int floor=0;\****	***\*//层数\****

​	***\*for(int i=0;i**
​		***\*cout<<" ";\****	***\*//输出前置空格\****
​	***\*char buf[256];\****
​	***\*int len=0;\****

​	***\*for(int i= strlen(folderPath)-1;folderPath[i]!='/';i--)\**** 
​		***\*buf[len++]=folderPath[i];\****
​	***\*buf[len]='\0';\****
​	***\*for(int i=0;i**
​		***\*char t=buf[i];\****
​		***\*buf[i]=buf[len-1-i];\****
​		***\*buf[len-1-i]=t;\****
​	***\*}\****
​	***\*cout<<"+--"<**
​	***\*DIR \*dir=opendir(folderPath);\****

​	***\*struct dirent \*i=NULL;\****

​	

​	***\*while((i=readdir(dir))!=NULL){\****

​		***\*if(!strcmp(i->d_name,".")||!strcmp(i->d_name,".."))//是文件的话调过\**** 

​			***\*continue;\****

​		***\*strcpy(buf,folderPath);\****

​		***\*strcat(buf,"/");\****

​		***\*strcat(buf,i->d_name);//进入下一级文件\**** 

​		

​		***\*struct stat M;\****

​		***\*stat(buf,&M);\****

​		

​		***\*if(S_ISDIR(M.st_mode)) //是目录\**** 

​		***\*{\****

​			***\*floor+=1;\****

​			***\*showDirStructure(buf);\****

​			***\*floor-=1;\****

​		***\*}\****

​		***\*else\****

​		***\*{\****

​			***\*if(S_ISREG(M.st_mode)){ //是文件\**** 

​				***\*char ext[256];\****

​				***\*len=0;\****

​				***\*for(int j=strlen(buf)-1;buf[j]!='.';j--)// 获取文件后缀\**** 

​					***\*ext[len++]=buf[j];\****

​				***\*ext[len]='\0';\****

​				***\*for(int j=0;j**

​					***\*char t=ext[j];\****

​					***\*ext[j]=ext[len-1-j];\****

​					***\*ext[len-1-j]=t;\****

​				***\*}\****

​				***\*if(!strcmp(ext,"jpg")||!strcmp(ext,"png")||!strcmp(ext,"bmp")){ //ext是图片\**** 

​					***\*for(int j=0;j<(floor+1)\*2;j++)\****

​						***\*cout<<" ";\****

​					***\*cout<<"--"

​				***\*}\****

​			***\*}\****

​		***\*}\****

​	***\*}\****

​	***\*closedir(dir);\****
```






### ***\*C++基础：各种输入方法总结，cin、cin.get()、cin.getline()、getline()、gets()、getchar()\****

cin通过使用空白（空格、制表符和换行符）来定字符串的界

cin.getline()函数读取整行，它使用通过回车键输入的换行符来确定输入结尾

### ***\*其他\****

\#include<stdio.h>

\#include<string.h>

\#include<stdlib.h>

\#include<ctype.h>

什么时候写，然后各种杂七杂八的原因报错

\#include<iostream>

\#include<string>

using namespace std;

 



 


第一章数组
1.1删除排序数组中的重复项
    // 1：首位可替换，重复就去除，长度要减一，然后重复检（后面的值代替前面的已经被检测出重复的值，有前移，下次检测的长度就减一，然后重新再按上次的检测位置重新检测）。

    for (int i = 1; i < len;)
	{
		if (nums[i] == nums[i - 1])
		{
			for (int j = i; j < len; j++) //不相等全部前移
				nums[j - 1] = nums[j];
			len--;
		}
		else
		{ //直到不相等
			i++;
		}
	}
	// 2	用count新建一个数组，遍历原来数组是否重复
	public
	static int removeDuplicates(int[] nums)
	{
		if (nums.length == 0)
			return 0;
		int count = 1;
		for (int i = 1; i < nums.length; i++)
		{
			if (nums[i - 1] != nums[i])
			{
				nums[count++] = nums[i];
			}
		}
		return count;

		//第二种实现方式
		/*if(nums.length == 0) return 0;
				int index=0;
				for(int i =1 ; i < nums.length ; i++){
					if ( nums[i] != nums[index]){
						index ++;
						nums[index] = nums[i];
					}
				}
				return ++index;*/
	}
		// 3 官方解法：方法：双指针法
		// 只要 nums[i]=nums[j]，我们就增加 j 以跳过重复项。
		// 当我们遇到 nums[j]≠nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复制到 nums[i + 1]。然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。

	public
	int removeDuplicates(int[] nums)
	{
		if (nums.length == 0)
			return 0;
		int i = 0;
		for (int j = 1; j < nums.length; j++)
		{
			if (nums[j] != nums[i])
			{
				i++;
				nums[i] = nums[j]; // nums[i]新数组记录
			}
		}
		return i + 1;
	}
	//4vector
	public:
	int removeDuplicates(vector<int> &nums)
	{
		return distance(nums.begin(), unique(nums.begin(), nums.end()));
	}
####################################################################################################################################################
1.2 删除排序数组中的重复项
	给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
	// 第一种思路：统计重复项，处理小二项，位置位递增，不同就覆盖（每检测到一个元素，我们需要统计下它的重复项有多少个，直到出现不同的元素，然后只处理一位，两位的元素，多余的元素不处理，位置位只有在处理元素是递增，遇到下一个不同的元素就按位置位覆盖）。
    public static int removeDuplicatesII(int[] nums) {
        if(nums.length <= 2) return nums.length;
		int pos = 1,flag = 1,int last = nums[0];
		for (int i = 1; i < nums.length; i++) {
			if (nums[i] == last) {
				flag++;
			} else {
				flag = 1;
			}
			if (flag <= 2) {
				nums[pos] = nums[i];//获取只有两个重复nums
				pos++;
			}
			last = nums[i];
		}
		return pos;
	}
####################################################################################################################################################
1.3-1.4买卖股票
	题干：
	给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
	如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
	注意你不能在买入股票前卖出股票。
	示例 1:

	输入: [7,1,5,3,6,4]    输出: 5
	输入: [7,6,4,3,1]    输出: 0 解释: 在这种情况下, 无交易完成, 所以最大利润为 0。

	第二种思路：单层循环，最小值可替换，选取最大值（我们先把最优解中的最小值初始设为首位元素，同时设置最大值变量，让最小值后的元素依次对最小值相减，直到遇到比它小的元素代替给当前最小值，取其中最大值赋值给最大值变量
		public static int maxProfit(int[] prices) {
			if (prices.length < 2) return 0;
			int min = prices[0];
			int result = 0;
			for (int i = 0; i < prices.length; i++) {
				if (prices[i] < min) {
					min = prices[i];
				} else if (prices[i] - min > result) {
					result = prices[i] - min;
				}
			}
			return result; 

	可以多次参与，但不能同时
	第二种思路：所有数组统一处理，定义最大利润变量，后者大前者就相减，差值加入最大利润，前者大于后者就忽略（我们将数组统一看待，然后定义一个最大利润变量，当所取元素的后一个元素大于所取元素，就后者减去前者，并把差值加入最大利润变量，若是前者大于后者，不做处理，直接从下一个元素继续以上操作，直至循环结束）。
	public static int maxProfit(int[] prices) {
		if (prices.length < 2) return 0;
		int sum = 0;
		for (int i = 0; i < prices.length - 1; i++) {
			if (prices[i] < prices[i + 1]) {
				sum += prices[i + 1] - prices[i];
			} else {
				continue;
			}
		}
		return sum;

####################################################################################################################################################
1.5 移动零
	// 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
	第一种思路：暴力破解，一步步向后
	public void moveZeroes(int[] nums) {
			int k = 0;
			for (int i = 0; i < nums.length - k; i++) {
				if (nums[i] == 0) {
					for (int j = i; j < nums.length - k - 1; j++) {
						nums[j] = nums[j + 1];//后面的数先前移
						nums[j + 1] = 0;//把0给后面的数，一步步向后
					}
					k++;
					i--;//再次检查刚才的替换点是否为零，多个0出现可能
				}
			}
		}
	第二种思路：覆盖0元素，0元素覆盖。


	public static void moveZeroes(int[] nums) {
		int count = 0;
		for (int i = 0; i < nums.length; i++) {
                        //第一种
			if (nums[i] == 0) {
				continue;
			}
			nums[count++] = nums[i];//先获取非0
                        //第二种
			/*if (nums[i] != 0) {
				nums[count++] = nums[i];
			}*/
		}
		while (count < nums.length) {
			nums[count++] = 0;
		}
	}
 ####################################################################################################################################################

1.6 区间子数组个数
	输入: 
		A = [2, 1, 4, 3]
		L = 2
		R = 3
		输出: 3
		解释: 满足条件的子数组: [2], [2, 1], [3].
	// 题干：
	// 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
	// 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。（数组要连续，有顺序
	第一种思路：暴力破解第一种思路代码：

		public int numSubarrayBoundedMax(int[] A, int L, int R) {
			int count = 0;
			for (int i = 0; i < A.length; i++) {
				int big = A[i];//有第一个
				for (int j = i; j < A.length; j++) {
					big = Math.max(big, A[j]);//最大的必须小于L，R才能count+
					if (big >= L && big <= R)
						count++;
				}
			}
			return count;
		}

	第二种思路代码：双指针法（滑动窗口法），遇到连续都属于 >= L 且 <= R 的数字，可作等差数列（a1 = 1，d = 1）,连续连续都属于 < L的数字且在此之前连续跟有 >= L 且 <= R 的数字，则可作为等比数列（a1 = 1，q = 1），遇	到 > R的数字则重新开始，双指针统一位置。如果更加节省时间，我们可以使用continue，但是再此之前双指针要进行重置，避免执行下面的判断，影响时间。(不是就很懂11.11)
	第二种思路代码：

    public int numSubarrayBoundedMax(int[] A, int L, int R) {
		int result = 0, left = -1, right = -1;
		for (int i = 0; i < A.length; i++) {
			if (A[i] > R)//大于R肯定大于L相减=0不要，<=R,>=L.
				left = i;
			if (A[i] >= L)
				right = i;
			result += right - left;
		}
		return result;
	}
####################################################################################################################################################
第二章 哈希表
2.1 两数之和
	给定 nums = [2, 7, 11, 15], target = 9
	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]
	方法一
		public static int[] twoSum(int[] nums, int target) {
			//将值，位置转换为key value存储
			HashMap<Integer, Integer> table = new HashMap<>();//HashMap<Integer, Integer> table = new HashMap<>();
			int[] result = new int[2];
			for (int i = 0; i < nums.length; i++) {
				if (table.get(target - nums[i]) != null) {
					result[0] = table.get(target - nums[i]);// table.get(a)
					result[1] = i;
					break;
				}

				table.put(nums[i], i);
			}
			return result;
		}
	方法二：异曲同工的代码:有的小伙伴或许会疑惑，为什么方法的最后没return，终止方法的众多方法中的两种简单的就是，return，抛出异常。而且这里如果执行到最后还没找到结果（虽然平台都不会这么无聊），返回不相干的数组肯定是不合适的，所以我们可以抛异常来终止程序。


		public static int[] twoSum(int[] nums, int target) {
			Map<Integer, Integer> map = new HashMap<>();
			for (int i = 0; i < nums.length; i++) {
				map.put(nums[i], i);
			}
			for (int i = 0; i < nums.length; i++) {
				int complement = target - nums[i];
				if (map.containsKey(complement) && map.get(complement) != i) {
					return new int[] { i, map.get(complement) };
				}
			}
			throw new IllegalArgumentException("No two sum solution");
		}


	####################################################################################################################################################

2.2 错误的集合（重复或者缺失

	输入: nums = [1,2,2,4]
	输出: [2,3]

	####################################################################################################################################################
	第三种思路变种：移形换影。创建另外的一个数组为boolean类型，根据值与位置的对应关系，用值代替位置（舍弃0位置，减少循环中的减运算），将值对应的位置设为true,重复值会对应同一位置，如若此位置的值已经是true，则此为重复值，最后再次遍历新数组（从1开始），如果某个值为false，则此处位置值就是被替换的值。
第三种思路变种代码：

	public int[] findErrorNums(int[] nums) {
		int[] result = new int[2];
		boolean[] array = new boolean[nums.length + 1];
		for (int num : nums) {
			if (array[num])
				result[0] = num;
			array[num] = true;
		}
		for (int i = 1; i < array.length; i++) {
			if (!array[i])
				result[1] = i;
		}
		return result;
	}


3 加1
	第一种思路：首先判断加一后是否需要进位，如果进位则继续循环，如不进位则循环结束，返回数组，在循环中设下进位标识符，若进位则进位标识符为true，当循环从头到尾，如果首位数字还需进位，此时应该新建数组，同时数组首位置为一，其他默认为零（这是所有原数组所有数字都为九的情况）。
	第一种思路代码：

		public static int[] plusOne(int[] digits) {
			boolean sign = false;
			for (int i = digits.length - 1; i >= 0; i--) {
				sign = false;
				if (digits[i] + 1 == 10) {
					digits[i] = 0;
					sign = true;
					continue;
				} else {
					digits[i] = digits[i] + 1;
					break;
				}
			}
			if (sign) {
				int nums[] = new int[digits.length + 1];
				nums[0] = 1;
				return nums;
			}
			return digits;

	第二种思路：不需进位标识符，我们只要从末尾数字到首位数字关注是否为九或者是否加一为十，首先判断末尾数字是否为九，若为九，则置为零，继续循环判断，直至到某一位置数字不为九，加一后返回数组或者直至循环结束，另外创建数字，首位数字置为一，其他默认为零（这是所有原数组所有数字都为九的情况）。
	第二种思路代码：

		public static int[] plusOne(int[] digits) {
			int len = digits.length;
			for (int i = len - 1; i >= 0; i--) {
				if (digits[i] == 9) {
					digits[i] = 0;
				} else {
					digits[i] += 1;
					return digits;
				}
			}
			int[] sum = new int[len + 1];
			sum[0] = 1;
			return sum;
		}


4.2 反转整数
	第一种思路：偷梁换柱——long类型代替int类型进行判断，最后返回值强转（long -> int）
	第一种思路代码：

		public int reverse(int x) {
			long sum = 0;
			while (x != 0) {
				int y = x % 10;
				sum = y + sum * 10;
				if (sum < Integer.MIN_VALUE || sum > Integer.MAX_VALUE) {
					return 0;
				}
				x = x / 10;
			}
			return (int) sum;
		}

		复杂度分析：
		时间复杂度：O(1)。
		空间复杂度：O(1)。
	第二种思路：提前发现，及时处理——在累加反转数字的步骤前进行提前预判。
	第二种思路代码：

	public int reverse(int x) {
		int sum = 0;
		while (x != 0) {
			int y = x % 10;
			if (sum < Integer.MIN_VALUE / 10 || sum > Integer.MAX_VALUE / 10) {
				return 0;
			}
			sum = y + sum * 10;
			x = x / 10;
		}
		return sum;



排列硬币
	n = 5
	硬币可排列成以下几行:
	¤
	¤ ¤
	¤ ¤
	因为第三行不完整，所以返回2.

6.1 整数转罗马数字
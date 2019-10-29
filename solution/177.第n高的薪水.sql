--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;--重要这一句

  RETURN (
      # Write your MySQL query statement below.
      select IFNULL((Select DISTINCT Salary from Employee order by Salary DESC LIMIT 1 OFFSET   N),NULL)

  );
END


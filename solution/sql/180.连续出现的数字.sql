--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--
# Write your MySQL query statement below
select count from (select Num ,count(*) as count from Logs group by Num) t where t.count>=3;


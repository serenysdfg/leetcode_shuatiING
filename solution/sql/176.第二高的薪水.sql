--
-- @lc app=leetcode.cn id=176 lang=mysql
--
-- [176] 第二高的薪水
--
# Write your MySQL query statement below

select IFNULL((select distinct(Salary) from Employee order by Salary desc limit 1 offset 1),NULL) as SecondHighestSalary;
--知识点IFNULL（expr1，null）
--limit 1 offset 1

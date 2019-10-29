--
-- @lc app=leetcode.cn id=185 lang=mysql
--
-- [185] 部门工资前三高的员工
--
-- https://leetcode-cn.com/problems/department-top-three-salaries/description/
--
-- database
-- Hard (29.00%)
-- Total Accepted:    5.1K
-- Total Submissions: 17.5K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Name", "Salary", "DepartmentId"], "Department": ["Id", "Name"]}, "rows": {"Employee": [[1, "Joe", 70000, 1], [2, "Henry", 80000, 2], [3, "Sam", 60000, 2], [4, "Max", 90000, 1]], "Department": [[1, "IT"], [2, "Sales"]]}}'
--
-- Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id 。
-- 
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- | 5  | Janet | 69000  | 1            |
-- | 6  | Randy | 85000  | 1            |
-- +----+-------+--------+--------------+
-- 
-- 
-- Department 表包含公司所有部门的信息。
-- 
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- 
-- 
-- 编写一个 SQL 查询，找出每个部门工资前三高的员工。例如，根据上述给定的表格，查询结果应返回：
-- 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Randy    | 85000  |
-- | IT         | Joe      | 70000  |
-- | Sales      | Henry    | 80000  |
-- | Sales      | Sam      | 60000  |
-- +------------+----------+--------+
-- 
-- 
--
-- 基于DepartmentId和Salary进行排序
-- 然后对相同部门的员工工资进行排序(特别注意: 如果工资相等, 那么排序应该也要相等)
-- 取出排序在前三的员工的信息
-- 将部门信息join起来
# Write your MySQL query statement below
SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM(
SELECT t.Name,
CASE
WHEN t.DepartmentId = @preDep THEN 
    CASE
    WHEN t.Salary = @preSal THEN @rank
    ELSE @rank := @rank + 1
    END
ELSE @rank := 1
END
AS rank,
@preDep := t.DepartmentId AS depId,
@preSal := t.Salary AS Salary
FROM
(SELECT * FROM Employee ORDER BY DepartmentId, Salary DESC) AS t, 
(SELECT @rank := 0, @preDep := -1, @preSal := -1) INIT
) AS e JOIN Department as d ON e.depId = d.Id WHERE e.rank <=3;


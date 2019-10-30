--
-- @lc app=leetcode.cn id=184 lang=mysql
--
-- [184] 部门工资最高的员工
--
-- https://leetcode-cn.com/problems/department-highest-salary/description/
--
-- database
-- Medium (33.08%)
-- Total Accepted:    7.4K
-- Total Submissions: 22.3K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Name", "Salary", "DepartmentId"], "Department": ["Id", "Name"]}, "rows": {"Employee": [[1, "Joe", 70000, 1], [2, "Henry", 80000, 2], [3, "Sam", 60000, 2], [4, "Max", 90000, 1]], "Department": [[1, "IT"], [2, "Sales"]]}}'
--
-- Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。
-- 
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- 
-- 
-- Department 表包含公司所有部门的信息。
-- 
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- 
-- 
-- 编写一个 SQL 查询，找出每个部门工资最高的员工。例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales
-- 部门有最高工资。
-- 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | Sales      | Henry    | 80000  |
-- +------------+----------+--------+
-- 
-- 
--
# Write your MySQL query statement below

select d.Name as Department, e.Name as Employee, e.Salary from Department d inner join

(select Employee.DepartmentId, Employee.Name, Employee.Salary from Employee, 

(select DepartmentId, max(Salary) as max_salary from Employee group by DepartmentId) as e 
where e.DepartmentId = Employee.DepartmentId and e.max_salary=Salary)  #找到最大

as e on e.DepartmentId = d.Id;


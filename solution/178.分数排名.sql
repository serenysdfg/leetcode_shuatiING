--
-- @lc app=leetcode.cn id=178 lang=mysql
--
-- [178] 分数排名
--
# Write your MySQL query statement below
SELECT Score, 
(SELECT count(DISTINCT score) FROM Scores WHERE score >= s.score) 
AS Rank FROM Scores s ORDER BY Score DESC;

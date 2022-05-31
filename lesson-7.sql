--SELECT score, `from` FROM tab1
--UNION SELECT val, type FROM tab2

SELECT score, 'table 1' as tbl FROM tab1 WHERE score IN(300, 400)
UNION SELECT val, 'table 2' FROM tab2
ORDER BY score DESC
LIMIT 3
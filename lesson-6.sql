-- SELECT lesson_5.name, lesson_5.sex, lesson_6.old FROM lesson_6, lesson_5

-- SELECT lesson_5.name, lesson_5.sex, lesson_6.old FROM lesson_5
-- JOIN lesson_6 ON lesson_5.user_id == lesson_6.user_id

-- SELECT lesson_5.name, lesson_5.sex, lesson_6.old FROM lesson_5
-- INNER JOIN lesson_6 ON lesson_5.user_id == lesson_6.user_id

-- SELECT lesson_5.name, lesson_5.sex, lesson_6.old FROM lesson_5
-- LEFT JOIN lesson_6 ON lesson_5.sex == lesson_6.sex


-- from self-edu lesson:
-- SELECT name, sex, sum(games.score) as score
-- FROM games
-- JOIN users ON games.user_id = users.rowid
-- GROUP BY user_id
-- ORDER BY score DESC
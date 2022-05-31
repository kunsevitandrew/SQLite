/*from self-edu*/

-- INSERT INTO female
-- SELECT NULL, name, sex, old FROM students WHERE sex = 2
--
-- UPDATE marks SET mark = 0
-- WHERE mark <= (SELECT min(mark) FROM marks WHERE id = 1)
--
-- DELETE FROM students
-- WHERE old < (SELECT old FROM students WHERE id = 2)


-- UPDATE lesson_8 SET col_2 =9999
-- WHERE col_2 < (SELECT col_2 FROM lesson_8 WHERE col_1 >0.5)
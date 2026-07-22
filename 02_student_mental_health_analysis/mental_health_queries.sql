-- Project: Student Mental Health Analysis
-- Purpose: Compare depression, social connectedness and acculturative stress scores by length of stay for international students

SELECT 
    stay, 
    COUNT(*) AS count_int, 
    ROUND(AVG(todep), 2) AS average_phq,
    ROUND(AVG(tosc), 2) AS average_scs, 
    ROUND(AVG(toas), 2) AS average_as
FROM students
WHERE LOWER(inter_dom) LIKE '%inter%'
GROUP BY stay
ORDER BY stay DESC;

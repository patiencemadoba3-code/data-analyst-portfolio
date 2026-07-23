-- =============================================
-- Project: LuxurStay Hotel Operations Analysis
-- Practical Exam: SQL Associate Certification
-- =============================================

-- TASK 1: Clean and validate branch data
SELECT
    id,
    COALESCE(location, 'Unknown') AS location,
    COALESCE(total_rooms, 100) AS total_rooms,
    COALESCE(staff_count, COALESCE(total_rooms, 100) * 1.5) AS staff_count,
    CASE
        WHEN opening_date = '-' OR opening_date IS NULL THEN '2023'
        ELSE opening_date
    END AS opening_date,
    CASE
        WHEN target_guests LIKE 'B%' THEN 'Business'
        ELSE 'Leisure'
    END AS target_guests
FROM branch;


-- TASK 2: Calculate average and max response time per branch and service
SELECT
    service_id,
    branch_id,
    ROUND(AVG(time_taken), 2) AS avg_time_taken,
    ROUND(MAX(time_taken), 2) AS max_time_taken
FROM request
GROUP BY service_id, branch_id;


-- TASK 3: Extract data for targeted regions and services
SELECT
    s.description,
    b.id,
    b.location,
    r.id AS request_id,
    r.rating
FROM request r
JOIN branch b ON r.branch_id = b.id
JOIN service s ON r.service_id = s.id
WHERE s.description IN ('Meal', 'Laundry')
  AND b.location IN ('EMEA', 'LATAM');


-- TASK 4: Identify underperforming services (rating below 4.5 target)
SELECT
    service_id,
    branch_id,
    ROUND(AVG(rating), 2) AS avg_rating
FROM request
GROUP BY service_id, branch_id
HAVING AVG(rating) < 4.5;

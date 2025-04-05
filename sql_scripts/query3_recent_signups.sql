SELECT *
FROM users
WHERE signup_date >= CURRENT_DATE - INTERVAL '7 days';

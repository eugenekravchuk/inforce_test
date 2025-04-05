WITH domain_counts AS (
    SELECT domain, COUNT(*) AS count
    FROM users
    GROUP BY domain
),
top_domain AS (
    SELECT domain
    FROM domain_counts
    ORDER BY count DESC
    LIMIT 1
)
SELECT *
FROM users
WHERE domain = (SELECT domain FROM top_domain);

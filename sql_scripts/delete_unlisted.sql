DELETE FROM users
WHERE domain NOT IN ('example.com', 'example.net', 'example.org');
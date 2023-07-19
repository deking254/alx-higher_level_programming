-- list the privileges of users user_0d_1 and user_02

SELECT
    CONCAT('SHOW GRANTS FOR \'', user, '\'@\'', host, '\';') AS show_grants_query
FROM
    mysql.user
WHERE
    user IN ('user_0d_1', 'user_0d_2')
    AND host = 'localhost';


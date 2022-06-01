# 196. Delete Duplicate Emails
# DELETE Table에 alias 달 때는 DELETE 뒤에는 alias만 쓰고 FROM에 Table이랑 alias 적어줌!
DELETE T1
FROM Person as T1
INNER JOIN Person T2 ON T1.email = T2.email
WHERE T1.id > T2.id
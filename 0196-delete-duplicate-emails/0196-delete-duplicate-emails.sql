# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
DELETE p from Person p
, Person q where p.Id>q.Id AND q.Email=p.Email 
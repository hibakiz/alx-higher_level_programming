--  script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM hbtn_0d_usa.states WHERE state_id = 1 ORDER BY id DES
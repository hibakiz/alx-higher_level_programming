--  script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id INTO @cal_id FROM states WHERE name = 'Calfornia';
SELECT id, name FROM cities WHERE state_id = @cal_id ORDER BY id;
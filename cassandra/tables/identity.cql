-- create identity table
CREATE TABLE neptune.identity (
    hr_id text PRIMARY KEY, 
    user_name text, 
    first_name text, 
    middle_name text, 
    last_name text, 
    job_title text, 
    location_number int, 
    location_name text, 
    manager_hr_id text
);
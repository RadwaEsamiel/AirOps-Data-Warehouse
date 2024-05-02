-- Create a sequence for auto-incrementing the primary key
CREATE SEQUENCE passenger_profile_key_seq
START WITH 1
MAXVALUE 9999999999999999999999999999
MINVALUE 1
NOCYCLE
NOCACHE
NOORDER;

-- Create table with the new column for frequent flyer status
CREATE TABLE dim_passenger_profile (
   profile_key NUMBER PRIMARY KEY,
   tier VARCHAR2(50),
   home_airport VARCHAR2(50),
   club_membership VARCHAR2(50),
   lifetime_mileage VARCHAR2(50),
   frequent_flyer_status VARCHAR2(50)  -- New column for status (e.g., "Blue," "Silver," etc.)
);

-- Create trigger to auto-increment the primary key
CREATE OR REPLACE TRIGGER trg_dim_passenger_profile
BEFORE INSERT ON dim_passenger_profile
FOR EACH ROW
BEGIN
   SELECT passenger_profile_key_seq.NEXTVAL INTO :new.profile_key FROM DUAL;
END;

-- Create sequence
CREATE SEQUENCE passenger_key_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

-- Create table using the sequence
CREATE TABLE dim_passenger (
    passenger_key NUMBER PRIMARY KEY,
    passenger_id VARCHAR2(20),
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    gender VARCHAR2(10),
    date_of_birth DATE,
    nationality VARCHAR2(50),
    country VARCHAR2(50),
    city VARCHAR2(50),
    marital_status VARCHAR2(20),
    income_level VARCHAR2(20)
);

-- Use the sequence to populate passenger_key
CREATE OR REPLACE TRIGGER trg_dim_passenger
BEFORE INSERT ON dim_passenger
FOR EACH ROW
BEGIN
    SELECT passenger_key_seq.NEXTVAL INTO :new.passenger_key FROM dual;
END;
/

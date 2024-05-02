-- Create sequence
CREATE SEQUENCE airport_key_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE TABLE dim_airport (
    Airport_Key NUMBER PRIMARY KEY,
    Airport_Id VARCHAR2(255),
    Airport_Name VARCHAR2(255),
    Country VARCHAR2(255),
    City VARCHAR2(255),
    Latitude NUMBER(10, 6),
    Longitude NUMBER(10, 6),
    Region VARCHAR2(100),
    Number_of_runways NUMBER,
    Terminal_count NUMBER,
    Number_of_gates NUMBER,
    ATC_capacity NUMBER,
    Aircraft_Parking_Stands NUMBER,
    Guest_Capacity NUMBER
);

-- Use the sequence to populate airport_key
CREATE OR REPLACE TRIGGER trg_dim_airport
BEFORE INSERT ON dim_airport
FOR EACH ROW
BEGIN
    SELECT airport_key_seq.NEXTVAL INTO :new.airport_key FROM dual;
END;
/

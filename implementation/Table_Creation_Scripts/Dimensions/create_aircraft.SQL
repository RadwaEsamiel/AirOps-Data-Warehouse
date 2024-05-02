/* Formatted on 4/29/2024 1:54:53 PM (QP5 v5.139.911.3011) */
-- Create sequence

CREATE SEQUENCE aircraft_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;

CREATE TABLE dim_aircraft (
    Aircraft_Key NUMBER PRIMARY KEY,
    Aircraft_Id VARCHAR2(255),
    Aircraft_Type VARCHAR2(255),
    Manufacturer VARCHAR2(255),
    Model VARCHAR2(255),
    Capacity NUMBER,
    Year_of_Manufacture NUMBER,
    Carrying_Weight NUMBER,
    Fuel_Consumption NUMBER
);

-- Use the sequence to populate aircraft_key

CREATE OR REPLACE TRIGGER trg_dim_aircraft
   BEFORE INSERT
   ON dim_aircraft
   FOR EACH ROW
BEGIN
   SELECT aircraft_key_seq.NEXTVAL
     INTO :new.aircraft_key
     FROM DUAL;
END;
/
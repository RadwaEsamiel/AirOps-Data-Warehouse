
CREATE SEQUENCE time_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;
   
CREATE TABLE dim_time (
    Time_Key NUMBER PRIMARY KEY,
    Hour NUMBER,
    Minute NUMBER,
    Daytime_Name VARCHAR2(255),
    Shifts VARCHAR2(255),
    Day_Night_Indicator VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER trg_dim_time
   BEFORE INSERT
   ON dim_time
   FOR EACH ROW
BEGIN
   SELECT time_key_seq.NEXTVAL
     INTO :new.Time_Key
     FROM DUAL;
END;
/
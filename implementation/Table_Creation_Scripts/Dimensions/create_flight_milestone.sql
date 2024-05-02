CREATE SEQUENCE flight_milestone_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;

CREATE TABLE dim_flight_milestone (
    Flight_Milestone_Key INTEGER PRIMARY KEY,
    Days_Before_Flight INTEGER,
    Marketed_Indicator VARCHAR2(50),
    Maintained_Indicator VARCHAR2(50),
    Crew_Scheduled_Indicator VARCHAR2(50),
    Fully_Booked_Indicator VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER trg_dim_flight_milestone
   BEFORE INSERT
   ON dim_flight_milestone
   FOR EACH ROW
BEGIN
   SELECT flight_milestone_key_seq.NEXTVAL
     INTO :new.flight_milestone_key
     FROM DUAL;
END;
/
CREATE SEQUENCE satisfaction_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;


CREATE TABLE dim_satisfaction (
    Satisfaction_Key NUMBER PRIMARY KEY,
    Delayed_Arrival_Indicator VARCHAR2(50),
    Airport_Divert_Indicator VARCHAR2(50),
    Lost_Luggage_Indicator VARCHAR2(50),
    Failed_to_Upgrade_Indicator VARCHAR2(50),
    Middle_Seat_Indicator VARCHAR2(50),
    Personnel_Problem_Indicator VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER trg_dim_satisfaction
   BEFORE INSERT
   ON dim_satisfaction
   FOR EACH ROW
BEGIN
   SELECT satisfaction_key_seq.NEXTVAL
     INTO :new.satisfaction_key
     FROM DUAL;
END;
/
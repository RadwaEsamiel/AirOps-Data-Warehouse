CREATE SEQUENCE class_of_service_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;


CREATE TABLE dim_class_of_service (
    Class_of_Service_Key NUMBER PRIMARY KEY,
    Class_Purchased VARCHAR2(255),
    Class_Flown VARCHAR2(255),
    Purchased_Flown_Group VARCHAR2(255),
    Class_Change_Indicator VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER trg_dim_class_of_service
   BEFORE INSERT
   ON dim_class_of_service
   FOR EACH ROW
BEGIN
   SELECT class_of_service_key_seq.NEXTVAL
     INTO :new.class_of_service_key
     FROM DUAL;
END;
/
CREATE SEQUENCE fare_basis_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;

CREATE TABLE dim_fare_basis (
    Fare_Basis_Key NUMBER PRIMARY KEY,
    Fare_Basis_Code VARCHAR2(255),
    Fare_Type VARCHAR2(255),
    Description VARCHAR2(255),
    Adv_Purchase_Days_Req NUMBER,
    Cancellation_Penalty VARCHAR2(255),
    Discount_Percentage NUMBER,
    Effective_Start_Date DATE,
    Effective_End_Date DATE,
    Applicable_Travel_Class VARCHAR2(255)
);

CREATE OR REPLACE TRIGGER trg_dim_fare_basis
   BEFORE INSERT
   ON dim_fare_basis
   FOR EACH ROW
BEGIN
   SELECT fare_basis_key_seq.NEXTVAL
     INTO :new.fare_basis_key
     FROM DUAL;
END;
/
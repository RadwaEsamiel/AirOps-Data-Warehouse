CREATE SEQUENCE city_pair_route_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;

drop table dim_city_pair_route;

CREATE TABLE dim_city_pair_route (
    City_Pair_Route_Key NUMBER PRIMARY KEY,
    Directional_Route_Name VARCHAR2(255),
    Non_Directional_Route_Name VARCHAR2(255),
    Route_Distance_in_Miles NUMBER,
    Route_Distance_Band VARCHAR2(255),
    Dom_Intl_Indicator VARCHAR2(25),
    Transocean_Indicator VARCHAR2(25)
);

CREATE OR REPLACE TRIGGER trg_dim_city_pair_route
   BEFORE INSERT
   ON dim_city_pair_route
   FOR EACH ROW
BEGIN
   SELECT city_pair_route_key_seq.NEXTVAL
     INTO :new.city_pair_route_key
     FROM DUAL;
END;
/
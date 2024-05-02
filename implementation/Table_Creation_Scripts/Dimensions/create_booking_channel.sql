/* Formatted on 4/29/2024 1:54:53 PM (QP5 v5.139.911.3011) */
-- Create sequence

CREATE SEQUENCE booking_channel_key_seq
   START WITH 1
   INCREMENT BY 1
   NOCACHE
   NOCYCLE;

CREATE TABLE dim_booking_channel
(
   booking_channel_key        NUMBER PRIMARY KEY,
   booking_channel_id         VARCHAR2 (255),
   Booking_channel_name       VARCHAR2 (255),
   booking_channel_type       VARCHAR2 (255),
   online_offline_indicator   VARCHAR2 (50)
);

-- Use the sequence to populate booking_channel_key

CREATE OR REPLACE TRIGGER trg_dim_booking_channel
   BEFORE INSERT
   ON dim_booking_channel
   FOR EACH ROW
BEGIN
   SELECT booking_channel_key_seq.NEXTVAL
     INTO :new.booking_channel_key
     FROM DUAL;
END;
/
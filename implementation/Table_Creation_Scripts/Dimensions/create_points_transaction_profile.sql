-- Create a sequence to generate unique keys for the table
CREATE SEQUENCE pts_tx_profile_key_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

-- Create the updated Points Activity dimension table
CREATE TABLE dim_points_transaction_profile (
    points_activity_key NUMBER PRIMARY KEY,  -- Primary key for this table
    source VARCHAR2(100),  -- Internal or external
    transaction_type VARCHAR2(10),  -- Type of transaction (e.g., earn, redeem, expiry)
    category VARCHAR2(100),  -- Category or Service category (e.g., Reservation, transportation, retail)
    sub_category VARCHAR2(100),  -- Sub-category or specific service (e.g., Uber ride, shopping spree)
    description VARCHAR2(255),  -- Description of the activity
    tier_level VARCHAR2(50),  -- Tier level (e.g., Basic, MidTier, WarriorTier)
    frequent_flyer_status VARCHAR2(50),  -- Frequent flyer status (e.g., Blue, Silver, etc.)
    company VARCHAR2(100)  -- Company involved in the transaction (e.g., ITI_Airlines)
);

-- Create a trigger to auto-increment the primary key using the sequence
CREATE OR REPLACE TRIGGER trg_dim_pts_tx_profile
BEFORE INSERT ON dim_points_transaction_profile
FOR EACH ROW
BEGIN
    SELECT pts_tx_profile_key_seq.NEXTVAL INTO :new.points_activity_key FROM DUAL;
END;
/

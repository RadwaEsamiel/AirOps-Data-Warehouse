-- Create a sequence to generate unique keys for the table
CREATE SEQUENCE tier_change_profile_key_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

-- Create the Tier Change dimension table
CREATE TABLE dim_tier_change_profile (
    tier_change_key NUMBER PRIMARY KEY,
    tier_name VARCHAR2(50),  -- Name of the tier (e.g., "Basic", "MidTier", "WarriorTier")
    frequent_flyer_status VARCHAR2(50),  -- Frequent flyer status (e.g., "Blue", "Silver", "Gold")
    is_active CHAR(1),  -- 'Y' or 'N' indicating if this tier is currently active
    is_upgrade CHAR(1),  -- 'Y' or 'N' indicating if this change represents an upgrade
    is_special_promotion CHAR(1)  -- 'Y' or 'N' indicating if this change is due to a special promotion
);

-- Create a trigger to auto-increment the primary key using the sequence
CREATE OR REPLACE TRIGGER trg_dim_tier_change_profile
BEFORE INSERT ON dim_tier_change_profile
FOR EACH ROW
BEGIN
    SELECT tier_change_profile_key_seq.NEXTVAL INTO :new.tier_change_key FROM DUAL;
END;
/

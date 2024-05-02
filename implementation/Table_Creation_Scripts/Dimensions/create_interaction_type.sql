-- Create sequence
CREATE SEQUENCE InteractionType_key_seq
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;


-- Create the Interaction Type dimension
CREATE TABLE dim_interaction_type (
    InteractionType_Key INT PRIMARY KEY,  
    InteractionType VARCHAR(100) NOT NULL,  
    Description VARCHAR(255),  
    SeverityLevel INT,  -- Represents the level of severity (e.g., 1 to 5)
   IsEscalable CHAR(1) -- Indicates if the interaction type can be escalated
);


CREATE OR REPLACE TRIGGER trg_dim_interaction_type
BEFORE INSERT ON dim_interaction_type
FOR EACH ROW
BEGIN
    SELECT InteractionType_key_seq.NEXTVAL INTO :new.InteractionType_Key FROM dual;
END;
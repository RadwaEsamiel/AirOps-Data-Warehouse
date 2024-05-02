-- Create the Communication Channel dimension
CREATE TABLE dim_communication_channel (
    CommunicationChannel_Key INT PRIMARY KEY,  
CustomKey VARCHAR(10),
    ChannelName VARCHAR(100) NOT NULL, 
    ChannelType VARCHAR(50), 
    Description VARCHAR(255),  
    IsActive CHAR(1) DEFAULT 'Y',  -- 'Y' or 'N' to indicate if the channel is active
    StartTime TIMESTAMP,  -- Time when the channel becomes available
    EndTime TIMESTAMP,  -- Time when the channel is no longer available
    TimeZone VARCHAR(50),  -- Time zone for the channel's availability times
    CustomerServiceHours VARCHAR(50)  -- Description of customer service hours (e.g., "9:00 AM - 5:00 PM")
);

-- Create a sequence to generate unique keys for the table
CREATE SEQUENCE CommunicationChannel_Key_Seq
START WITH 1
INCREMENT BY 1;

-- Create a trigger to auto-increment the primary key using the sequence
CREATE OR REPLACE TRIGGER trg_dim_CommunicationChannel
BEFORE INSERT ON dim_communication_channel
FOR EACH ROW
BEGIN
    SELECT CommunicationChannel_Key_Seq.NEXTVAL INTO :new.CommunicationChannel_Key FROM dual;
END;

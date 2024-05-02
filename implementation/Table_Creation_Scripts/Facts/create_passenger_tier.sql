CREATE TABLE fact_passenger_tier (
    passenger_key INT,  -- Foreign key referencing the Passenger dimension
    date_key INT,  -- Foreign key referencing the Date dimension
    time_key INT,  -- Foreign key referencing the Time dimension
    passenger_profile_key INT,  -- Foreign key referencing the Passenger Profile dimension
    tier_change_key INT  -- Foreign key referencing the Tier Change dimension
);
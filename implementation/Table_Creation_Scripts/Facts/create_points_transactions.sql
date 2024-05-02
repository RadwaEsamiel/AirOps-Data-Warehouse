/* Formatted on 4/29/2024 10:26:30 PM (QP5 v5.139.911.3011) */
CREATE TABLE fact_Points_transaction
(
   passenger_key                    INT, -- Foreign key referencing the Passenger dimension
   passenger_profile_key            INT, -- Foreign key referencing the Passenger Profile dimension
   date_key                         INT, -- Foreign key referencing the Date dimension
   time_key                         INT, -- Foreign key referencing the Time dimension
   POINTS_TRANSACTION_PROFILE_KEY   INT, -- Foreign key referencing the Points Activity dimension
   points_total                     NUMERIC (10, 2) -- Measure for the total points
);
/* Formatted on 4/30/2024 11:16:15 AM (QP5 v5.139.911.3011) */
CREATE TABLE fact_flight_revenue
(
   Scheduled_Departure_Date_Key   INTEGER,
   Scheduled_Departure_Time_Key   INTEGER,
   Origin_Airport_Key             INTEGER,
   Destination_Airport_Key        INTEGER,
   Flight_Milestone_Key           INTEGER,
   Aircraft_Key                   INTEGER,
   Flight_Number                  VARCHAR2 (50),
   Unearned_Revenue               NUMBER (15, 2),
   Remaining_Economy_Seats        INTEGER,
   Remaining_Prem_Economy_Seats   INTEGER,
   Remaining_Business_Seats       INTEGER,
   Remaining_First_Class_Seats    INTEGER,
   Cancelled_Reservations         INTEGER
);
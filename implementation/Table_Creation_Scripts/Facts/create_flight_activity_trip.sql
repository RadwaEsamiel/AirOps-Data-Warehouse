CREATE TABLE fact_flight_activity_trip (
    Segment_Origin_Airport_Key NUMBER,
    Segment_Dest_Airport_Key NUMBER,
    Booking_Channel_Key NUMBER,
    Scheduled_Departure_Date_Key NUMBER,
    Scheduled_Departure_Time_Key NUMBER,
    Actual_Departure_Date_Key NUMBER,
    Actual_Departure_Time_Key NUMBER,
    Passenger_Key NUMBER,
    Passenger_Profile_Key NUMBER,
    Confirmation_Number_DD VARCHAR2(6),
    Base_Fare_Revenue NUMBER(10,3),
    Overnight_Stay NUMBER,
    Passenger_Facility_Charges NUMBER(10,3),
    Airport_Tax NUMBER(10,3),
    Government_Tax NUMBER(10,3),
    Baggage_Charges NUMBER(10,3),
    Upgrade_Fees NUMBER(10,3),
    Transaction_Fees NUMBER(10,3),
    Segment_Miles_Flown NUMBER(10,3),
    Segment_Miles_Earned NUMBER(10,3),
    Trip_Duration NUMBER(10,3),
    Overnight_Stay_Duration NUMBER(10,3),
    Delay_Duration NUMBER(10,3)
);

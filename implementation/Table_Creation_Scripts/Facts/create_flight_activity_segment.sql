
CREATE TABLE fact_flight_activity_segment (
    Scheduled_Departure_Date_Key NUMBER,
    Scheduled_Departure_Time_Key NUMBER,
    Actual_Departure_Date_Key NUMBER,
    Actual_Departure_Time_Key NUMBER,
  
    Passenger_Key NUMBER,
    Passenger_Profile_Key NUMBER,
  
    Segment_Origin_Airport_Key NUMBER,
    Segment_Dest_Airport_Key NUMBER,
    Aircraft_Key NUMBER,
   Class_of_Service_Flown_Key NUMBER,
    Fare_Basis_Key NUMBER,
   Booking_Channel_Key NUMBER,
    Confirmation_Number_DD NUMBER,
    Ticket_Number_DD NUMBER,
    Segment_Sequence_Number_DD NUMBER,
    Flight_Number_DD VARCHAR2(50),
    Base_Fare_Revenue NUMBER(10,3),
    Passenger_Facility_Charges NUMBER(10,3),
    Airport_Tax NUMBER(10,3),
    Government_Tax NUMBER(10,3),
    Baggage_Charges NUMBER(10,3),
    Upgrade_Fees NUMBER(10,3),
    Transaction_Fees NUMBER(10,3),
    Segment_Miles_Flown NUMBER(10,3),
    Segment_Miles_Earned NUMBER(10,3)
  
  );

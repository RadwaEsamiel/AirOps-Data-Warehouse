CREATE TABLE dim_date (
  date_key NUMBER PRIMARY KEY,
  full_date DATE NOT NULL,
  day_of_week VARCHAR2(20),
  day_of_month NUMBER,
  day_of_year NUMBER,
  week_number NUMBER,
  month VARCHAR2(20),
  quarter NUMBER,
  year NUMBER,
  holiday_indicator VARCHAR2(10),  -- Adjust size based on your needs
  weekday_weekend_indicator VARCHAR2(20),
  season VARCHAR2(20),
  fiscal_period VARCHAR2(20),
  fiscal_year NUMBER,
  financial_period VARCHAR2(20),
  financial_year NUMBER,
  quarter_start_date DATE,
  quarter_end_date DATE,
  month_start_date DATE,
  month_end_date DATE,
  week_start_date DATE,
  week_end_date DATE,
  day_type VARCHAR2(20),  -- Working Day, Weekend, Holiday
  leap_year_indicator VARCHAR2(5)  -- Yes/No
);

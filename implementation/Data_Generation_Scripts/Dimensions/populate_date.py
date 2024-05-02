import datetime
import random


def get_season(month):
    if month in [1, 2, 12]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Unknown'

def get_fiscal_period(month):
    if month in [1, 2, 3]:
        return 'Q1'
    elif month in [4, 5, 6]:
        return 'Q2'
    elif month in [7, 8, 9]:
        return 'Q3'
    elif month in [10, 11, 12]:
        return 'Q4'
    else:
        return 'Unknown'

def get_financial_period(month):
    # Assuming financial year starts from January
    return f'M{month}'

def get_fiscal_year(year, month):
    if month in [10, 11, 12]:  # Fiscal year starts from October
        return year + 1
    else:
        return year

def get_financial_year(year):
    return year


# Function to generate insert statements
def generate_insert(date):
    date_key = int(date.strftime('%Y%m%d')) 
    full_date = date.strftime('%Y-%m-%d')
    day_of_week = date.strftime('%A')
    day_of_month = date.day
    day_of_year = date.timetuple().tm_yday
    week_number = date.isocalendar()[1]
    month = date.strftime('%B')
    quarter = (date.month - 1) // 3 + 1
    year = date.year
    
    # Randomly assign holiday indicator
    if random.random() < 0.05:  # 5% chance
        holiday_indicator = 'Y'
    else:
        holiday_indicator = 'N'
    
    weekday_weekend_indicator = 'Weekend' if date.weekday() in [5, 6] else 'Weekday'
    season = get_season(date.month)
    fiscal_period = get_fiscal_period(date.month)
    fiscal_year = get_fiscal_year(date.year, date.month)
    financial_period = get_financial_period(date.month)
    financial_year = get_financial_year(date.year)
    quarter_start_date = datetime.date(year, 3 * quarter - 2, 1)
    quarter_end_date = datetime.date(year, 3 * quarter, 1) - datetime.timedelta(days=1)
    month_start_date = datetime.date(year, date.month, 1)
    month_end_date = datetime.date(year, date.month % 12 + 1, 1) - datetime.timedelta(days=1)
    week_start_date = date - datetime.timedelta(days=date.weekday())
    week_end_date = date + datetime.timedelta(days=6-date.weekday())
    day_type = 'Weekend' if date.weekday() in [5, 6] else 'Working Day'
    leap_year_indicator = 'Yes' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 'No'

    insert_statement = f"INSERT INTO dim_date VALUES ({date_key}, TO_DATE('{full_date}', 'YYYY-MM-DD'), '{day_of_week}', {day_of_month}, {day_of_year}, {week_number}, '{month}', {quarter}, {year}, '{holiday_indicator}', '{weekday_weekend_indicator}', '{season}', '{fiscal_period}', {fiscal_year}, '{financial_period}', {financial_year}, TO_DATE('{quarter_start_date}', 'YYYY-MM-DD'), TO_DATE('{quarter_end_date}', 'YYYY-MM-DD'), TO_DATE('{month_start_date}', 'YYYY-MM-DD'), TO_DATE('{month_end_date}', 'YYYY-MM-DD'), TO_DATE('{week_start_date}', 'YYYY-MM-DD'), TO_DATE('{week_end_date}', 'YYYY-MM-DD'), '{day_type}', '{leap_year_indicator}');\n"
    return insert_statement

# Define start and end dates
start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2023, 12, 31)

# Generate insert statements for each day
with open('populate_date.SQL', 'w') as data:
    current_date = start_date
    while current_date <= end_date:
        insert_statement = generate_insert(current_date)
        try:
            data.write(insert_statement)
        except:
            continue    
        current_date += datetime.timedelta(days=1)


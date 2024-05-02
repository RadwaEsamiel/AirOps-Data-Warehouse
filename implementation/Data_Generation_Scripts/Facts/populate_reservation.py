import random
from datetime import datetime, timedelta


# Define ranges for each item
aircraft_range = (1, 100)
date_range = (20140101, 20231231)
airport_range = (1, 37)
booking_channel_range = (1, 100)
time_range = (1, 1440)
passenger_profile_range = (1, 1200)
passenger_range = (9929, 19854)
class_of_service_range = (1, 64)
city_pair_route_range = (290, 93595)
fare_basis_range = (1, 500)
communication_channel_range = (1009, 1512)
satisfaction_range = (1, 64)
interaction_type_range = (1, 50)
transaction_profile_range = (1, 999)

def generate_random_date_key():
    # Define start and end dates
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate a random date within the specified range
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Convert the random date to an integer in the format YYYYMMDD
    date_key = int(random_date.strftime('%Y%m%d'))
    
    return date_key

# Function to generate random decimal value within a range
def random_decimal(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

# Function to generate random insert statement
def generate_insert():
    insert_statement = "INSERT INTO fact_reservations VALUES ("
    insert_statement += str(generate_random_date_key()) + ", "
    insert_statement += str(random.randint(time_range[0], time_range[1])) + ", "
    insert_statement += str(random.randint(passenger_range[0], passenger_range[1])) + ", "
    insert_statement += str(random.randint(passenger_profile_range[0], passenger_profile_range[1])) + ", "
    insert_statement += str(random.randint(airport_range[0], airport_range[1])) + ", "
    insert_statement += str(random.randint(airport_range[0], airport_range[1])) + ", "
    insert_statement += str(random.randint(aircraft_range[0], aircraft_range[1])) + ", "
    insert_statement += str(random.randint(class_of_service_range[0], class_of_service_range[1])) + ", "
    insert_statement += str(random.randint(fare_basis_range[0], fare_basis_range[1])) + ", "
    insert_statement += str(random.randint(booking_channel_range[0], booking_channel_range[1])) + ", "
    insert_statement += str(random.randint(city_pair_route_range[0], city_pair_route_range[1])) + ", "
    insert_statement += "'" + ''.join(random.choices('0123456789', k=10)) + "', " # Confirmation_Number
    insert_statement += str(random.randint(1, 10)) + ", " # Segment_Sequence_Number
    insert_statement += "'" + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6)) + "', " # Flight_Number
    insert_statement += str(random_decimal(50, 500)) + ", " # Base_Fare_Revenue
    insert_statement += str(random_decimal(10, 50)) + ", " # Passenger_Facility_Charges
    insert_statement += str(random_decimal(5, 30)) + ", " # Airport_Tax
    insert_statement += str(random_decimal(5, 50)) + ", " # Government_Tax
    insert_statement += str(random_decimal(2, 10)) # Transaction_Fees
    insert_statement += ");\n"
    return insert_statement

with open('populate_reservations.sql', 'w') as data:
    for _ in range(100000):
        insertaya = generate_insert()
        try:
            data.write(insertaya)
        except:
            continue
        
            

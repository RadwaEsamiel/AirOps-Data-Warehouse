import random
from datetime import datetime, timedelta


# Define ranges for each item
airport_key_range = (1, 37)
flight_milestone_key_range = (1, 2160)  # Changed to 2160 as per your requirement
aircraft_key_range = (1, 100)
flight_number_length = 50
unearned_revenue_range = (0, 100000)
remaining_seats_range = (0, 300)
cancelled_reservations_range = (0, 50)

def generate_random_date_key():
    # Define start and end dates
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate a random date within the specified range
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Convert the random date to an integer in the format YYYYMMDD
    date_key = int(random_date.strftime('%Y%m%d'))
    
    return date_key

# Function to generate random flight number
def generate_flight_number():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=flight_number_length))

# Function to generate random decimal value within a range
def random_decimal(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

# Function to generate random non-duplicate flight milestone keys for a flight number
def generate_flight_milestone_keys():
    return random.sample(range(1, flight_milestone_key_range[1] + 1), 90)

# Function to generate random insert statements
def generate_insert(flight_number, departure_date_key, departure_time_key, flight_milestone_keys):
    insert_statements = []
    for milestone_key in flight_milestone_keys:
        insert_statement = "INSERT INTO fact_flight_revenue VALUES ("
        insert_statement += str(departure_date_key) + ", "
        insert_statement += str(departure_time_key) + ", "
        insert_statement += str(random.randint(airport_key_range[0], airport_key_range[1])) + ", "
        insert_statement += str(random.randint(airport_key_range[0], airport_key_range[1])) + ", "
        insert_statement += str(milestone_key) + ", "
        insert_statement += str(random.randint(aircraft_key_range[0], aircraft_key_range[1])) + ", "
        insert_statement += "'" + flight_number + "', "
        insert_statement += str(random_decimal(unearned_revenue_range[0], unearned_revenue_range[1])) + ", "
        insert_statement += str(random.randint(remaining_seats_range[0], remaining_seats_range[1])) + ", "
        insert_statement += str(random.randint(remaining_seats_range[0], remaining_seats_range[1])) + ", "
        insert_statement += str(random.randint(remaining_seats_range[0], remaining_seats_range[1])) + ", "
        insert_statement += str(random.randint(remaining_seats_range[0], remaining_seats_range[1])) + ", "
        insert_statement += str(random.randint(cancelled_reservations_range[0], cancelled_reservations_range[1]))
        insert_statement += ");\n"
        insert_statements.append(insert_statement)
    return insert_statements

with open('populate_flight_revenue.SQL', 'w') as data:
    for _ in range(1000):
        flight_number = generate_flight_number()
        departure_date_key = generate_random_date_key()
        departure_time_key = random.randint(1, 1440)
        flight_milestone_keys = generate_flight_milestone_keys()
        insert_statements = generate_insert(flight_number, departure_date_key, departure_time_key, flight_milestone_keys)
        for statement in insert_statements:
            data.write(statement);


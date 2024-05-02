import random
from datetime import datetime, timedelta

def generate_random_date_key():
    # Define start and end dates
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate a random date within the specified range
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Convert the random date to an integer in the format YYYYMMDD
    date_key = int(random_date.strftime('%Y%m%d'))
    
    return date_key


# Define ranges for each item
passenger_key_range = (9929, 19854)
passenger_profile_key_range = (1, 1200)
date_key_range = (20140101, 20231231)
time_key_range = (1, 1440)
points_transaction_profile_key_range = (1, 5000)


# Function to generate random decimal value within a range
def random_decimal(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

# Function to generate random insert statement
def generate_insert():
    insert_statement = "INSERT INTO fact_points_transactions VALUES ("
    insert_statement += str(random.randint(passenger_key_range[0], passenger_key_range[1])) + ", "
    insert_statement += str(random.randint(passenger_profile_key_range[0], passenger_profile_key_range[1])) + ", "
    insert_statement += str(generate_random_date_key()) + ", "
    insert_statement += str(random.randint(time_key_range[0], time_key_range[1])) + ", "
    insert_statement += str(random.randint(1, points_transaction_profile_key_range[1])) + ", "
    insert_statement += str(random_decimal(0, 10000)) # Assuming points_total range
    insert_statement += ");\n"
    return insert_statement

with open('populate_points_transactions.sql', 'w') as data:
    for _ in range(50000):
        insertaya = generate_insert()
        try:
            data.write(insertaya)
        except:
            continue

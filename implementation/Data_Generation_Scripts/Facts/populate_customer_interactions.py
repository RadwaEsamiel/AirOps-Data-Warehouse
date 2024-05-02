import random
from datetime import datetime, timedelta

# Define ranges for each item
passenger_key_range = (9929, 19854)
profile_key_range = (1, 1200)
communication_channel_range = (1009, 1512)
date_range = (20140101, 20231231)
time_range = (1, 1440)
interaction_type_range = (1, 50)
interaction_rating_range = (1.0, 10.0)

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
    insert_statement = "INSERT INTO AIRLINE_DW.FACT_CUSTOMER_INTERACTION VALUES ("
    insert_statement += str(random.randint(interaction_type_range[0], interaction_type_range[1])) + ", "
    insert_statement += str(random.randint(passenger_key_range[0], passenger_key_range[1])) + ", "
    insert_statement += str(random.randint(profile_key_range[0], profile_key_range[1])) + ", "
    insert_statement += str(random.randint(communication_channel_range[0], communication_channel_range[1])) + ", "
    insert_statement += str(generate_random_date_key()) + ", "
    insert_statement += str(random.randint(time_range[0], time_range[1])) + ", "
    insert_statement += str(random_decimal(interaction_rating_range[0], interaction_rating_range[1]))
    insert_statement += ");\n"
    return insert_statement

with open('populate_customer_interactions.sql', 'w') as data:
    for _ in range(20000):
        insertaya = generate_insert()
        try:
            data.write(insertaya)
        except:
            continue
        
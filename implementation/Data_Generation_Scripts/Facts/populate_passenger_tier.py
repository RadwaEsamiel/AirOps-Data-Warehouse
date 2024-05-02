import random
from datetime import datetime, timedelta

# Define key ranges for the Passenger Tier Data fact table
passenger_key_range = (1, 5000)  # Possible passenger key values
profile_key_range = (1, 150)  # Possible profile key values
time_range = (1, 1440)  # 1440 minutes in a day
tier_change_key_range = range(1,40)  # Even numbers from 2 to 80

# Function to generate a random date key in the correct format
def generate_date_key():
    # Define the date range from January 1, 2014, to December 31, 2023
    start_date = datetime(2014, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate a random date within this range
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Convert the random date to an integer in the format YYYYMMDD
    date_key = int(random_date.strftime('%Y%m%d'))
    return date_key

# Function to generate random insert statement for fact_passenger_tier_data
def generate_insert():
    insert_statement = "INSERT INTO fact_passenger_tier values ("
    insert_statement += str(random.randint(passenger_key_range[0], passenger_key_range[1])) + ", "
    insert_statement += str(generate_date_key()) + ", "  # Use the updated date logic
    insert_statement += str(random.randint(time_range[0], time_range[1])) + ", "
    insert_statement += str(random.randint(profile_key_range[0], profile_key_range[1])) + ", "
    insert_statement += str(random.choice(tier_change_key_range))  # Random even number between 2 and 80
    insert_statement += ");\n"
    return insert_statement

# Generate SQL INSERT INTO statements to populate the Passenger Tier Data fact table
with open("populate_passenger_tier.sql", "w") as data:
    for _ in range(2000):  # Generate 2000 insert statements
        try:
            insert_statement = generate_insert()  # Generate a random insert statement
            data.write(insert_statement)  # Write to the output file
        except Exception as e:
            print(f"Error writing to file: {e}")  # Handle exceptions

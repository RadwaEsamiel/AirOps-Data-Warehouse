# Import necessary libraries
import random
import string

def generate_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))  # Two uppercase letters
    suffix = ''.join(random.choices(string.digits, k=3))  # Three digits
    return f"{prefix}-{suffix}"

channel_names = ["Email", "Phone", "SMS", "Live Chat", "Social Media", "Mobile App", "In-Person"]
channel_types = ["Digital", "Voice", "Text"]
is_active_options = ["Y", "N"]
time_zones = ["PST", "MST", "CST", "EST"]
customer_service_hours = ["9:00 AM - 5:00 PM", "24/7", "6:00 AM - 10:00 PM"]

default_start_time = "TO_TIMESTAMP('09:00:00', 'HH24:MI:SS')"
default_end_time = "TO_TIMESTAMP('17:00:00', 'HH24:MI:SS')"

insert_statements = []

for channel_name in channel_names:
    for channel_type in channel_types:
        for is_active in is_active_options:
            for time_zone in time_zones:
                for hours in customer_service_hours:
                    custom_key = generate_id()  # Generate a custom surrogate key
                    insert_statement = (
                        "INSERT INTO dim_CommunicationChannel (CommunicationChannel_Key, CustomKey, ChannelName, ChannelType, Description, IsActive, StartTime, EndTime, TimeZone, CustomerServiceHours) "
                        f"VALUES (CommunicationChannel_Key_Seq.NEXTVAL, '{custom_key}', '{channel_name}', '{channel_type}', 'Description for {channel_name}', '{is_active}', {default_start_time}, {default_end_time}, '{time_zone}', '{hours}');"
                    )
                    insert_statements.append(insert_statement)

for statement in insert_statements:
    print(statement)

with open("CommunicationChannel_population.sql", "w") as file:
    file.write("\n".join(insert_statements))

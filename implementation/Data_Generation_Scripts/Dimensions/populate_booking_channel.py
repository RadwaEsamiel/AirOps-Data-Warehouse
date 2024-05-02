from datetime import datetime, timedelta
import random
import string

# Values for Booking_channel_name
booking_channel_names = [
    "Online Website",
    "Mobile App",
    "Travel Agency",
    "Call Center",
    "Kiosk",
    "Social Media Platform",
    "Airline Office",
    "Hotel Booking Site",
    "Car Rental Site",
    "Cruise Booking Site"
]

# Values for booking_channel_type
booking_channel_types = [
    "Direct",
    "Indirect",
    "OTA (Online Travel Agency)",
    "Meta Search",
    "GDS (Global Distribution System)",
    "TMC (Travel Management Company)",
    "Metasearch",
    "Corporate",
    "Leisure",
    "Other"
]

offline_list = ["offline", "online"]

def generate_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}-{suffix}"

with open('populate_booking_channel.sql', 'w') as data:
    for channel_name in booking_channel_names:
        for channel_type in booking_channel_types:
            booking_channel_id = generate_id()
            online_offline_indicator = random.choice(offline_list)
            insert_statement = f"INSERT INTO dim_booking_channel VALUES (1, '{booking_channel_id}', '{channel_name}', '{channel_type}', '{online_offline_indicator}');\n"
            try:
                data.write(insert_statement)
            except:
                continue

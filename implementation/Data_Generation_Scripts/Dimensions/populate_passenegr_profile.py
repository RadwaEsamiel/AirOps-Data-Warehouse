import random

# Define possible values for tier, club membership, lifetime mileage
tier = ["Basic", "MidTier", "WarriorTier"]
club_membership = ["Club Member", "Non-Member"]
lifetime_mileage = ["Under 100,000 miles", "100,000-499,999 miles", "1,000,000-1,999,999 miles", "2,000,000-2,999,999 miles"]
states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
        'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ]

# Define a function to determine the frequent flyer status based on tier
def get_frequent_flyer_status(tier):
    if tier == "Basic":
        return "Blue"
    elif tier == "MidTier":
        return random.choice(["Silver", "Gold"])
    elif tier == "WarriorTier":
        return random.choice(["Platinum", "Titanium"])

# Function to generate SQL INSERT statements to populate dim_passenger_profile
def populate_profile():
    with open("populate_passenger_profile.SQL", "w") as data:
        for t in tier:
            for c in club_membership:
                for l in lifetime_mileage:
                    for s in states:
                        # Get the appropriate frequent flyer status based on tier
                        frequent_flyer_status = get_frequent_flyer_status(t)
                        
                        insert_statement = (
                            "INSERT INTO dim_passenger_profile "
                            "(profile_key, tier, home_airport, club_membership, lifetime_mileage, frequent_flyer_status) "
                            f"VALUES (passenger_profile_key_seq.NEXTVAL, '{t}', '{s}', '{c}', '{l}', '{frequent_flyer_status}');\n"
                        )
                        
                        data.write(insert_statement)  # Write to the output file

# Call the function to generate the SQL insert statements
populate_profile()

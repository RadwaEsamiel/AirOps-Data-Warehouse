import random



# Define possible transaction types
transaction_types = ["earn", "redeem", "expiry"]

# Define possible categories and sub-categories
categories = ["Reservation", "Special Occasion", "Complaint Resolution", "Offers and Promotions"]
service_categories = ["transportation", "retail", "food", "entertainment", "appliances and electronics"]

sub_categories = {
    "Reservation": ["Flight Booking", "Hotel Booking"],
    "Special Occasion": ["National Holiday", "InterNational Holiday", "Birthday"],
    "Complaint Resolution": ["Resolved", "Compensated"],
    "Offers and Promotions": ["Discount", "Bonus Points"],
    "transportation": ["flight", "uber ride", "train journey", "car rental"],
    "retail": ["fancy dinner", "shopping spree", "electronics purchase", "furniture shopping"],
    "food": ["restaurant meal", "takeout order", "coffee", "dessert"],
    "entertainment": ["cinema ticket", "concert ticket", "amusement park visit", "museum entry"],
    "appliances and electronics": ["television", "laptop", "washing machine", "smartphone"]
}

# Define other possible values for attributes
tier_levels = ["Basic", "MidTier", "WarriorTier"]
frequent_flyer_statuses = {
    "Basic": ["Blue"],
    "MidTier": ["Silver", "Gold"],
    "WarriorTier": ["Platinum", "Titanium"]
}

# Generate SQL INSERT INTO statements to populate the Points Activity dimension
def generate_insert_statements(num_rows):
    with open("populate_points_transaction_profile.sql", "w") as data:
        for i in range(1, num_rows + 1):
            source = "internal" if random.random() < 0.5 else "external"
            transaction_type = random.choice(transaction_types)
            category = random.choice(service_categories) if source == "external" else random.choice(categories)
            sub_category = random.choice(sub_categories[category])
            description = f"{category} - {sub_category} activity"
            tier_level = random.choice(tier_levels)
            frequent_flyer_status = random.choice(frequent_flyer_statuses[tier_level])
            company = "ITI_Airlines" if source == "internal" else f"{category}_company{random.randint(1, 4)}"

            # Adjusted INSERT INTO statement to include transaction_key
            insert_statement = (
                "INSERT INTO dim_points_transaction_profile "
                f"VALUES ('1','{source}', '{transaction_type}', '{category}', '{sub_category}', '{description}', '{tier_level}', '{frequent_flyer_status}', '{company}');\n"
            )

            data.write(insert_statement)  # Write to the output file

generate_insert_statements(5000) 

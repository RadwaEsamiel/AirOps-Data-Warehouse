import random

# Define possible values for each attribute in the Tier Change dimension
tier_names = ["Basic", "MidTier", "WarriorTier"]
frequent_flyer_statuses = {
    "Basic": ["Blue"],
    "MidTier": ["Silver", "Gold"],
    "WarriorTier": ["Platinum", "Titanium"]
}
is_active_options = ["Y", "N"]
is_upgrade_options = ["Y", "N"]
is_special_promotion_options = ["Y", "N"]

# Function to generate SQL INSERT INTO statements for the Tier Change dimension
def generate_insert_statements():
    with open("populate_tier_change_profile.sql", "w") as data:
        # Loop through each tier and its corresponding frequent flyer statuses
        for tier_name in tier_names:
            for frequent_flyer_status in frequent_flyer_statuses[tier_name]:
                for is_active in is_active_options:
                    for is_upgrade in is_upgrade_options:
                        for is_special_promotion in is_special_promotion_options:
                            # Create the SQL INSERT statement
                            insert_statement = (
                                "INSERT INTO dim_tier_change "
                                f"(tier_change_key, tier_name, frequent_flyer_status, is_active, is_upgrade, is_special_promotion) "
                                f"VALUES ('1', '{tier_name}', '{frequent_flyer_status}', '{is_active}', '{is_upgrade}', '{is_special_promotion}');\n"
                            )
                            
                            data.write(insert_statement)  # Write the insert statement to the file

# Generate the SQL insert statements to populate the Tier Change dimension
generate_insert_statements()

# Function to generate insert statements for dim_flight_milestone table
def generate_insert_statements():
    insert_statements = []
    for days in range(90, 0, -1):
        for marketed in ["Yes", "No"]:
            for maintained in ["Maintained", "Not Maintained", "In Maintenance"]:
                for crew_scheduled in ["Scheduled", "Not Scheduled"]:
                    for fully_booked in ["Fully Booked", "Not Fully Booked"]:
                        insert_statement = "INSERT INTO dim_flight_milestone (Flight_Milestone_Key, Days_Before_Flight, Marketed_Indicator, Maintained_Indicator, Crew_Scheduled_Indicator, Fully_Booked_Indicator) VALUES "
                        values = f"(NULL, {days}, '{marketed}', '{maintained}', '{crew_scheduled}', '{fully_booked}');\n"
                        insert_statements.append(insert_statement + values)
    return insert_statements

# Generate insert statements
insert_statements = generate_insert_statements()

with open('populate_flight_milestone.sql', 'w') as data:
    for statement in insert_statements:
        data.write(statement)

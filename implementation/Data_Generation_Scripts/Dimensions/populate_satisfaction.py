

def generate_insert(satisfaction_key, delayed_arrival, airport_divert, lost_luggage, failed_to_upgrade, middle_seat, personnel_problem):
    insert_statement = f"INSERT INTO dim_satisfaction VALUES ({satisfaction_key}, '{delayed_arrival}', '{airport_divert}', '{lost_luggage}', '{failed_to_upgrade}', '{middle_seat}', '{personnel_problem}');\n"
    return insert_statement

# Generate insert statements for all possible combinations
with open('populate_satisfaction.SQL', 'w') as data:
    for delayed_arrival in ['Yes', 'No']:
        for airport_divert in ['Yes', 'No']:
            for lost_luggage in ['Yes', 'No']:
                for failed_to_upgrade in ['Yes', 'No']:
                    for middle_seat in ['Yes', 'No']:
                        for personnel_problem in ['Yes', 'No']:
                            insert_statement = generate_insert('1', delayed_arrival, airport_divert, lost_luggage, failed_to_upgrade, middle_seat, personnel_problem)
                            try:
                                data.write(insert_statement)
                            except:
                                continue



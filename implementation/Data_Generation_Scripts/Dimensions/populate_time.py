def generate_insert(time_key, hour, minute, daytime_name, shifts, day_night_indicator):
    insert_statement = f"INSERT INTO dim_time VALUES ('1', {hour}, {minute}, '{daytime_name}', '{shifts}', '{day_night_indicator}');\n"
    return insert_statement


with open('populate_time.SQL', 'w') as data:
    for hour in range(24):
        for minute in range(60):
            time_key = hour * 100 + minute  # Generating a time key in the format HHMM
            daytime_name = "Morning" if hour < 12 else "Afternoon" if hour < 18 else "Evening"
            shifts = "Shift 1" if hour < 8 else "Shift 2" if hour < 16 else "Shift 3"
            day_night_indicator = "Day" if 6 <= hour < 18 else "Night"
            insert_statement = generate_insert(time_key, hour, minute, daytime_name, shifts, day_night_indicator)
            try:
                data.write(insert_statement)
            except:
                continue    
        


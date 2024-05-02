from datetime import datetime, timedelta
import random
import string

last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
    "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis",
    "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez",
    "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
    "Perez", "Sanchez", "Ramirez", "Flores", "Rivera", "Gomez", "Diaz", "Reyes",
    "Stewart", "Morales", "Murphy", "Cook", "Rogers", "Morgan", "Peterson", "Cooper",
    "Reed", "Bailey", "Bell", "Gutierrez", "Gonzales", "Sanders", "Ross", "Howard",
    "Kim", "Collins", "Cruz", "Parker", "Evans", "Edwards", "Collins", "Roberts",
    "Turner", "Phillips", "Campbell", "Perez", "Murray", "Washington", "Coleman",
    "Hughes", "Long", "Foster", "Ward", "Torres", "Murphy", "Reed", "Bailey",
    "Watson", "Russell", "Bryant", "Alexander", "Griffin", "Dunn", "Ford", "Grant",
    "Mendoza", "Curtis", "Reyes", "Chavez", "Sullivan", "Sullivan", "Simmons", "Woods",
    "Garcia", "Pierce", "Hawkins", "Hart", "Hunt", "Chen", "Snyder", "Stone", "Hunt",
    "Arnold", "Perkins", "Black", "Bates", "Larson", "Dixon", "Holmes"
]

first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James",
    "Isabella", "Oliver", "Charlotte", "Elijah", "Amelia", "Benjamin", "Mia",
    "Lucas", "Harper", "Mason", "Evelyn", "Logan", "Abigail", "Alexander", "Emily",
    "Ethan", "Elizabeth", "Jacob", "Mila", "Michael", "Ella", "Daniel", "Avery",
    "Henry", "Sofia", "Jackson", "Camila", "Sebastian", "Aria", "Aiden", "Scarlett",
    "Matthew", "Victoria", "Lily", "Liam", "Grace", "Jack", "Chloe", "Alexander", "Sophie", "Lucas",
    "Ava", "Joshua", "Zoe", "Caleb", "Madison", "Samuel", "Natalie", "Dylan",
    "Layla", "Nathan", "Hannah", "Carter", "Brooklyn", "Evan", "Audrey", "Gabriel",
    "Lillian", "Isaac", "Stella", "Ryan", "Violet", "Luke", "Savannah", "Aiden",
    "Addison", "Isaiah", "Eleanor", "Owen", "Hailey", "Andrew", "Skylar", "David",
    "Alyssa", "Leah", "John", "Ariana", "Nathan", "Brianna", "Jason", "Megan", "Christopher",
    "Samantha", "Nicholas", "Kayla", "Brandon", "Allison", "Tyler", "Makayla", "Christian",
    "Gabrielle", "Justin", "Alexis", "Austin", "Rachel", "Jonathan", "Julia", "Jose",
    "Vanessa", "Kevin", "Lauren", "Daniel", "Anna", "Jose", "Nicole", "Eric", "Jordan",
    "Ashley", "Brian", "Emma", "Thomas", "Jasmine", "Zachary", "Michelle", "Connor", "Maya", "Derek", "Sara", "Eli", "Claire", "Mason", "Ruby",
    "Cole", "Nora", "Adrian", "Alice", "Colton", "Elena", "Tristan", "Leila",
    "Dominic", "Haley", "Bryce", "Jocelyn", "Victor", "Alexa", "Preston", "Katherine",
    "Jaxon", "Caroline", "Julian", "Samantha", "Miles", "Grace", "Felix", "Elise",
    "Everett", "Amaya", "Micah", "Lydia", "Gavin", "Hannah", "Landon", "Avery"
]


countries = {
    'US': [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
        'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ],
    'England': ['London', 'Birmingham', 'Manchester', 'Liverpool', 'Bristol'],
    'Scotland': ['Glasgow', 'Edinburgh', 'Aberdeen', 'Dundee', 'Inverness'],
    'Wales': ['Cardiff', 'Swansea', 'Newport', 'Bangor', 'St Davids'],
    'Northern Ireland': ['Belfast', 'Derry', 'Lisburn', 'Newry', 'Armagh'],
    'Australia': [
        'New South Wales',
        'Australian Capital Territory',
        'Northern Territory',
        'Queensland',
        'South Australia',
        'Tasmania',
        'Victoria',
        'Western Australia'
    ],
    'Spain': [
        'Andalusia', 'Aragon', 'Asturias', 'Balearic Islands', 'Basque Country',
        'Canary Islands', 'Cantabria', 'Castile and León', 'Castilla-La Mancha',
        'Catalonia', 'Extremadura', 'Galicia', 'La Rioja', 'Madrid', 'Murcia',
        'Navarre', 'Valencian Community'
    ],
    'Germany': [
        'Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg',
        'Hesse', 'Lower Saxony', 'Mecklenburg-Vorpommern', 'North Rhine-Westphalia',
        'Rhineland-Palatinate', 'Saarland', 'Saxony', 'Saxony-Anhalt', 'Schleswig-Holstein',
        'Thuringia'
    ],
    'France': [
        'Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comté', 'Brittany', 'Centre-Val de Loire',
        'Corsica', 'Grand Est', 'Hauts-de-France', 'Île-de-France', 'Normandy', 'Nouvelle-Aquitaine',
        'Occitanie', 'Pays de la Loire', 'Provence-Alpes-Côte d\'Azur'
    ]
}

marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
income_levels = [
    "Below $20,000", "$20,000 - $40,000", "$40,000 - $60,000", "$60,000 - $80,000",
    "$80,000 - $100,000", "$100,000 - $120,000", "$120,000 - $150,000", "Above $150,000"
]

def random_date_of_birth():
    start_date = datetime(1960, 1, 1)
    end_date = datetime.now() - timedelta(days=365*18)  # At least 18 years old
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

def generate_passenger_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}-{suffix}"



def generate_insert_statement():
    with open('Populate_Passenger.SQL', 'w') as data:
        for i in range(10000):
            passenger_id = generate_passenger_id()
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            gender = random.choice(["Male", "Female"])
            date_of_birth = random_date_of_birth().strftime('%Y-%m-%d')
            nationality = random.choice(list(countries.keys()))
            country = random.choice(list(countries.keys()))
            city = random.choice(countries[country])
            marital_status = random.choice(marital_statuses)
            income_level = random.choice(income_levels)

            insert_statement = (
            f"INSERT INTO DIM_PASSENGER "
            f"VALUES ('1', '{passenger_id}', '{first_name}', '{last_name}', '{gender}', TO_DATE('{date_of_birth}', 'YYYY-MM-DD'), "
            f"'{nationality}', '{country}', '{city}', '{marital_status}', '{income_level}');\n"
            )
            try:
                print('b3ml')
                data.write(insert_statement)
            except:
                print('no')
                continue
generate_insert_statement()






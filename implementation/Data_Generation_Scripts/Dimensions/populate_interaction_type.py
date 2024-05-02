# Updated script to align with CHAR(1) for boolean values in Oracle
# Define possible interaction types and their attributes
interaction_types = [
    "Inquiry",
    "Complaint",
    "Feedback",
    "Technical Support",
    "Refund Request",
    "Lost Baggage",
    "Flight Delay",
    "Service Request",
    "Promotion Inquiry",
    "Special Assistance",
]

interaction_descriptions = {
    "Inquiry": "General customer inquiries",
    "Complaint": "Customer complaints",
    "Feedback": "Customer feedback",
    "Technical Support": "Technical support",
    "Refund Request": "Requests for ticket refunds",
    "Lost Baggage": "Reports of lost or delayed baggage",
    "Flight Delay": "Complaints about flight delays",
    "Service Request": "Requests for specific services",
    "Promotion Inquiry": "Inquiries about promotions",
    "Special Assistance": "Requests for special assistance",
}

insert_statements = []

# Generate all combinations of interaction types and severity levels
interaction_type_key = 1

for interaction_type in interaction_types:
    description = interaction_descriptions[interaction_type]

    for severity_level in range(1, 6):
        # Determine if the interaction type is escalable (here, 'Y' if severity >= 3, 'N' otherwise)
        is_escalable = 'Y' if severity_level >= 3 else 'N'

        insert_statement = (
            "INSERT INTO dim_InteractionType (InteractionType_Key, InteractionType, Description, SeverityLevel, IsEscalable) "
            f"VALUES ({interaction_type_key}, '{interaction_type}', '{description}', {severity_level}, '{is_escalable}');"
        )

        insert_statements.append(insert_statement)
        interaction_type_key += 1

# Output the generated insert statements
for statement in insert_statements:
    print(statement)

# Optionally, write the insert statements to a file for execution in your SQL environment
with open("InteractionType_populate.sql", "w") as file:
    file.write("\n".join(insert_statements))

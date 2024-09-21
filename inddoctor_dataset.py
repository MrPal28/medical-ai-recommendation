import pandas as pd
import random
from faker import Faker

# Initializing faker 
fake = Faker('en_IN')

# Number of doctors
total_doctors = 300

# Generating random Indian doctor names using Faker
doctor_names = [fake.name() for _ in range(total_doctors)]

# List of  Indian cities 
indian_cities = [
    'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 
    'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur', 'Lucknow', 
    'Kanpur', 'Nagpur', 'Indore', 'Bhopal', 'Patna', 'Ludhiana', 'Agra'
]

#  data for the doctors
data = {
    'DoctorID': [f'Doc{str(i).zfill(3)}' for i in range(1, total_doctors + 1)],  # Unique IDs for doctors
    'Name': doctor_names,  
    'Specialization': random.choices(
        ['Cardiologist', 'Pediatrician', 'Dermatologist', 'Orthopedic', 'Neurologist','Oncologist','Pulmonologist','Endocrinologist','Gastroenterologist','Nephrologist','Hematologist','Rheumatologist','Infectious Disease Specialist','ENT Specialist','Allergist/Immunologist'], k=total_doctors),  # Random specializations
    'Experience': [random.randint(1, 40) for _ in range(total_doctors)],  # Random experience years between 1 and 40
    'Location': random.choices(indian_cities, k=total_doctors),  # Randomly chosen Indian cities
    'Rating': [round(random.uniform(1, 5), 1) for _ in range(total_doctors)]  # Random ratings between 1.0 and 5.0
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Reorder the columns to place Rating as the last column
df = df[['DoctorID', 'Name', 'Specialization', 'Experience', 'Location', 'Rating']]

# Save the DataFrame to a CSV file
df.to_csv('indian_doctors_dataset_with_locations_and_rating_last.csv', index=False)

print("Dummy Indian doctor dataset created and saved to 'indian_doctors_dataset_with_locations_and_rating_last.csv'")

# Suggest Doctors Algo

import pandas as pd
# Load the dataset
doctor_df = pd.read_csv(r"C:\Users\ARINDAM PAL\OneDrive\Desktop\MODEL\remeet\Doctor_data_with_diseases.csv")

# Function to recommend doctors based on disease
def suggest_doctors(disease, doctors_df, sort_by="both"):
    # Filter doctors by disease (search within the 'Diseases' column)
    filtered_doctors = doctors_df[doctors_df['Diseases'].str.contains(disease, case=False, na=False)]
    if filtered_doctors.empty:
        return f"No doctors found for the disease: {disease}"
    # Sort doctors by experience or rating
    if sort_by == 'experience':
        sorted_doctors = filtered_doctors.sort_values(by='Experience', ascending=False)
    elif sort_by == 'rating':
        sorted_doctors = filtered_doctors.sort_values(by='Rating', ascending=False)
    elif sort_by == 'both':
        sorted_doctors = filtered_doctors.sort_values(by=['Experience', 'Rating'], ascending=[False, False])
    
    # Return the sorted list of doctors
    return sorted_doctors
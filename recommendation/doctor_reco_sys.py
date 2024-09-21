# Doctor Recomendation According to Experience and Rating

import pandas as pd
import json
doctor_df=pd.read_csv(r"C:\Users\ARINDAM PAL\OneDrive\Desktop\ML RECOMENDATION\medical-ai-recommendation\indian_doctors_dataset_with_locations_and_rating_last.csv")

disease_df=pd.read_csv(r"C:\Users\ARINDAM PAL\OneDrive\Desktop\ML RECOMENDATION\medical-ai-recommendation\disease_symptom_dataset_50.csv")

# doctor_df["Specialization"].unique()
# array(['ENT Specialist', 'Infectious Disease Specialist', 'Pediatrician',
#        'Oncologist', 'Allergist/Immunologist', 'Gastroenterologist',
#        'Cardiologist', 'Orthopedic', 'Dermatologist', 'Hematologist',
#        'Neurologist', 'Endocrinologist', 'Nephrologist', 'Rheumatologist',
#       'Pulmonologist'], dtype=object)


# disease_df["Disease"].unique()
# array(['Heart Attack', 'Hypertension', 'Arrhythmia',
#        'Coronary Artery Disease', 'Atherosclerosis', 'Cardiomyopathy',
#        'Heart Failure', 'Pericarditis', 'Aortic Aneurysm',
#        'Valvular Heart Disease', 'Asthma', 'Bronchiolitis', 'Pneumonia',
#        'Whooping Cough', 'Chickenpox', 'Measles', 'Mumps', 'Croup',
#        'Hand-Foot-Mouth Disease', 'Tonsillitis', 'Eczema', 'Psoriasis',
#        'Acne', 'Rosacea', 'Melanoma', 'Contact Dermatitis',
#        'Fungal Infection', 'Vitiligo', 'Alopecia', 'Hives',
#        'Osteoarthritis', 'Rheumatoid Arthritis', 'Osteoporosis',
#        'Fractures', 'Sprains', 'Dislocations', 'Tendonitis', 'Scoliosis',
#        'Carpal Tunnel Syndrome', 'Bone Cancer', 'Alzheimer’s Disease',
#        'Parkinson’s Disease', 'Multiple Sclerosis', 'Stroke', 'Epilepsy',
#        'Migraines', 'Amyotrophic Lateral Sclerosis (ALS)', 'Brain Tumor',
#        'Guillain-Barré Syndrome', 'Neuropathy'], dtype=object)




# Dictionary mapping diseases to the respective doctor specialization
disease_to_specialization = {
    'Heart Attack': 'Cardiologist',
    'Hypertension': 'Cardiologist',
    'Arrhythmia': 'Cardiologist',
    'Coronary Artery Disease': 'Cardiologist',
    'Atherosclerosis': 'Cardiologist',
    'Cardiomyopathy': 'Cardiologist',
    'Heart Failure': 'Cardiologist',
    'Pericarditis': 'Cardiologist',
    'Aortic Aneurysm': 'Cardiologist',
    'Valvular Heart Disease': 'Cardiologist',
    
    'Asthma': 'Pulmonologist',
    'Bronchiolitis': 'Pulmonologist',
    'Pneumonia': 'Pulmonologist',
    'Whooping Cough': 'Pulmonologist',
    
    'Chickenpox': 'Pediatrician',
    'Measles': 'Pediatrician',
    'Mumps': 'Pediatrician',
    'Croup': 'Pediatrician',
    'Hand-Foot-Mouth Disease': 'Pediatrician',
    'Tonsillitis': 'ENT Specialist',
    
    'Eczema': 'Dermatologist',
    'Psoriasis': 'Dermatologist',
    'Acne': 'Dermatologist',
    'Rosacea': 'Dermatologist',
    'Melanoma': 'Oncologist',
    'Contact Dermatitis': 'Dermatologist',
    'Fungal Infection': 'Dermatologist',
    'Vitiligo': 'Dermatologist',
    'Alopecia': 'Dermatologist',
    'Hives': 'Dermatologist',
    
    'Osteoarthritis': 'Orthopedic',
    'Rheumatoid Arthritis': 'Rheumatologist',
    'Osteoporosis': 'Endocrinologist',
    'Fractures': 'Orthopedic',
    'Sprains': 'Orthopedic',
    'Dislocations': 'Orthopedic',
    'Tendonitis': 'Orthopedic',
    'Scoliosis': 'Orthopedic',
    'Carpal Tunnel Syndrome': 'Orthopedic',
    
    'Bone Cancer': 'Oncologist',
    'Alzheimer’s Disease': 'Neurologist',
    'Parkinson’s Disease': 'Neurologist',
    'Multiple Sclerosis': 'Neurologist',
    'Stroke': 'Neurologist',
    'Epilepsy': 'Neurologist',
    'Migraines': 'Neurologist',
    'Amyotrophic Lateral Sclerosis (ALS)': 'Neurologist',
    'Brain Tumor': 'Oncologist',
    'Guillain-Barré Syndrome': 'Neurologist',
    'Neuropathy': 'Neurologist'
}
# Function to get the specialization based on disease
def get_specialization(disease):
    return disease_to_specialization.get(disease, "Specialization not found")


# Function to recommend doctors based on disease

def recommend_doctors(disease, doctors_df, sort_by="both"):
    """
  Recommend doctors based on disease and user's preference for sorting.

  Parameters:
  - disease: Disease input from user.
  - doctors_df: DataFrame containing doctor details.
  - sort_by: Optional string ('experience', 'rating', or 'both') to determine the sorting.

  Returns:
  - A sorted DataFrame of doctors based on the user's selection.
""" # Get the specialization for the disease
    specialization = get_specialization(disease)

    if specialization == "Specialization not found":
        return "Sorry, we couldn't find any doctors for the disease '{}'.".format(disease)
   

    # Filter doctors based on specialization
    doctors_for_specialization = doctors_df[doctors_df['Specialization'] == specialization]

    # Sort based on user preference
    if sort_by == "experience":
        sorted_doctors = doctors_for_specialization.sort_values(by='Experience', ascending=False)
    elif sort_by == "rating":
        sorted_doctors = doctors_for_specialization.sort_values(by='Rating', ascending=False)
    else:  # Sort by both experience and rating
        sorted_doctors = doctors_for_specialization.sort_values(by=['Experience', 'Rating'], ascending=[False, False])
    
    return sorted_doctors

# Function to format output as JSON
def format_as_json(recommended_doctors):
    if recommended_doctors.empty:
        return json.dumps({"message": "No doctors found"})
    
    doctors_data = recommended_doctors[['Name', 'Specialization', 'Experience', 'Location', 'Rating']].to_dict(orient='records')
    return json.dumps(doctors_data, indent=4)


# # Main function to handle execution
# def main():
#     disease_input = input("Enter the disease name: ")
#     sort_preference = input("Sort by experience, rating, or both? (default: both): ") or "both"

#     recommended_doctors = recommend_doctors(disease_input, doctor_df, sort_by=sort_preference)
    
#     if isinstance(recommended_doctors, str):  # Check if it's an error message
#         print(recommended_doctors)
#     else:
#         doctors_json = format_as_json(recommended_doctors)
#         print(doctors_json)

# if __name__ == "__main__":
#     main()
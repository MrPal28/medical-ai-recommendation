import pandas as pd

#  50 diseases with 3 symptoms each 
data = {
    'Disease': [
        'Heart Attack', 'Hypertension', 'Arrhythmia', 'Coronary Artery Disease', 'Atherosclerosis', 
        'Cardiomyopathy', 'Heart Failure', 'Pericarditis', 'Aortic Aneurysm', 'Valvular Heart Disease',
        'Asthma', 'Bronchiolitis', 'Pneumonia', 'Whooping Cough', 'Chickenpox', 
        'Measles', 'Mumps', 'Croup', 'Hand-Foot-Mouth Disease', 'Tonsillitis',
        'Eczema', 'Psoriasis', 'Acne', 'Rosacea', 'Melanoma', 
        'Contact Dermatitis', 'Fungal Infection', 'Vitiligo', 'Alopecia', 'Hives',
        'Osteoarthritis', 'Rheumatoid Arthritis', 'Osteoporosis', 'Fractures', 'Sprains',
        'Dislocations', 'Tendonitis', 'Scoliosis', 'Carpal Tunnel Syndrome', 'Bone Cancer',
        'Alzheimer’s Disease', 'Parkinson’s Disease', 'Multiple Sclerosis', 'Stroke', 'Epilepsy', 
        'Migraines', 'Amyotrophic Lateral Sclerosis (ALS)', 'Brain Tumor', 'Guillain-Barré Syndrome', 'Neuropathy'
    ],
    'Symptom1': [
        'Chest Pain', 'Headache', 'Palpitations', 'Shortness of Breath', 'Chest Pain',
        'Fatigue', 'Swelling in Legs', 'Chest Pain', 'Back Pain', 'Shortness of Breath',
        'Coughing', 'Wheezing', 'Fever', 'Cough', 'Rash',
        'Rash', 'Swollen Glands', 'Barking Cough', 'Fever', 'Sore Throat',
        'Itchy Skin', 'Thickened Skin', 'Pimples', 'Facial Redness', 'Dark Spots',
        'Itching', 'Redness', 'Skin Discoloration', 'Hair Loss', 'Swelling',
        'Joint Pain', 'Swollen Joints', 'Bone Pain', 'Severe Pain', 'Joint Pain',
        'Deformity', 'Pain in Joints', 'Curved Spine', 'Wrist Pain', 'Bone Pain',
        'Memory Loss', 'Tremors', 'Numbness', 'Weakness', 'Seizures',
        'Severe Headache', 'Muscle Weakness', 'Seizures', 'Weakness', 'Numbness'
    ],
    'Symptom2': [
        'Shortness of Breath', 'Dizziness', 'Fatigue', 'Chest Pain', 'Leg Pain',
        'Palpitations', 'Shortness of Breath', 'Fever', 'Abdominal Pain', 'Fatigue',
        'Wheezing', 'Shortness of Breath', 'Chest Pain', 'Vomiting', 'Fever',
        'Cough', 'Fever', 'Difficulty Breathing', 'Blisters', 'Fever',
        'Redness', 'Red Patches', 'Pustules', 'Bumps', 'Moles',
        'Blisters', 'Peeling Skin', 'White Patches', 'Thinning Hair', 'Red Bumps',
        'Stiffness', 'Joint Swelling', 'Loss of Height', 'Swelling', 'Swelling',
        'Bruising', 'Tenderness', 'Back Pain', 'Tingling', 'Swelling',
        'Confusion', 'Slow Movements', 'Fatigue', 'Paralysis', 'Aura Sensations',
        'Nausea', 'Muscle Twitching', 'Headache', 'Tingling', 'Burning Sensation'
    ],
    'Symptom3': [
        'Fatigue', 'Nosebleeds', 'Dizziness', 'Fatigue', 'Numbness',
        'Irregular Heartbeat', 'Nausea', 'Cough', 'Weakness', 'Swelling',
        'Fatigue', 'Vomiting', 'Sweating', 'Fatigue', 'Itching',
        'Runny Nose', 'Headache', 'Hoarseness', 'Rash', 'Trouble Swallowing',
        'Cracked Skin', 'Scaly Skin', 'Swelling', 'Flushing', 'Enlarged Moles',
        'Burning', 'Cracked Skin', 'Hair Graying', 'Bald Spots', 'Itchy Skin',
        'Bone Loss', 'Joint Deformity', 'Fractures', 'Bruising', 'Bruising',
        'Pain', 'Limited Range of Motion', 'Hip Pain', 'Weak Grip', 'Fractures',
        'Disorientation', 'Rigidity', 'Muscle Weakness', 'Loss of Balance', 'Staring Spells',
        'Sensitivity to Light', 'Difficulty Speaking', 'Blurred Vision', 'Loss of Reflexes', 'Burning'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('disease_symptom_dataset_50.csv', index=False)

print("Dummy dataset with 50 diseases and symptoms saved to 'disease_symptom_dataset_50.csv'")
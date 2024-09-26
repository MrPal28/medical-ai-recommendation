##This is an integrated Version of how the model work with algo 

import numpy as np 
import pandas as pd 
import matplotlib as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ARINDAM PAL\OneDrive\Desktop\MODEL\check\Training.csv")
len(data['prognosis'].unique())
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

x=data.drop("prognosis",axis=1)
y=data['prognosis']
le=LabelEncoder()
le.fit(y)
Y=le.transform(y)

x_train,x_test,y_train,y_test=train_test_split(x,Y,test_size=0.3,random_state=20)

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier ,GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, confusion_matrix

# created a dictionary to run everything at once 
models = {
    "SVC":SVC(kernel='linear'),
     "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
     'GradientBoosting': GradientBoostingClassifier(n_estimators=100,random_state=42),
     "KNeighbors": KNeighborsClassifier(n_neighbors=5),
     "MultinomialNB": MultinomialNB()

}
for model_name ,model in models.items():
 model.fit(x_train,y_train)
predictions = model.predict(x_test)
accuracy= accuracy_score(y_test,predictions)
cm=confusion_matrix(y_test,predictions)

print(f"{model_name} accuracy :{accuracy}")
print(f"{model_name}  confusion matrix ")
print(np.array2string(cm, separator=','))



svc= SVC(kernel='linear')
svc.fit(x_train,y_train)
ypred=svc.predict(x_test)
accuracy_score(y_test,ypred)


import pickle  
pickle.dump(svc,open(r"svc.pkl",'wb'))


svc=pickle.load(open(r"svc.pkl",'rb'))


print ("model predicted label:",svc.predict(x_test.iloc[0].values.reshape(1,-1)))  #test1
print("actual label ",y_test[0])

print ("model predicted label:",svc.predict(x_test.iloc[10].values.reshape(1,-1)))  #test2
print("actual label ",y_test[10])


symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}


diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}


#model function to take symptom and return the disease
def get_disease(patient_symptoms):
   input_vector= np.zeros(len(symptoms_dict))

   for item in patient_symptoms:
      input_vector[symptoms_dict[item]]=1
      return diseases_list[svc.predict([input_vector])[0]]
   

   # Load the dataset
doctor_df = pd.read_csv(r"C:\Users\ARINDAM PAL\OneDrive\Desktop\MODEL\check\Doctor_data_with_diseases.csv")

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


symptoms= input("enter your symptoms: ").lower()
user_symptoms=[s.strip() for s in  symptoms.split(',')]
user_symptoms=[sym.strip("[]'") for sym in user_symptoms]
predicted = get_disease(user_symptoms)


print(predicted)



suggested_doctors = suggest_doctors(predicted, doctor_df, 'rating')
print(suggested_doctors)
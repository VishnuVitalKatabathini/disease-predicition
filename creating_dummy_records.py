import random
import pandas as pd
df=pd.read_csv('archive/dataset.csv')
# Generate dummy doctor data for each disease
unique_diseases = df["Disease"].unique()
doctors = []
doctor_id = 101  # Starting ID

for disease in unique_diseases:
    doctor_name = f"Dr. {random.choice(['Amit', 'Sneha', 'Rajesh', 'Priya', 'Vikram', 'Neha', 'Arjun', 'Kavita', 'Rahul', 'Divya'])} {random.choice(['Sharma', 'Patel', 'Singh', 'Mehta', 'Kapoor', 'Verma'])}"
    experience = random.randint(5, 25)  # Experience between 5 and 25 years
    contact_no = str(random.randint(9000000000, 9999999999))  # Random 10-digit phone number
    doctors.append((doctor_id, doctor_name, experience, disease, contact_no))
    doctor_id += 1  # Increment ID

# Convert to DataFrame for preview
doctors_df = pd.DataFrame(doctors, columns=["Doctor ID", "Name", "Experience", "Specialization", "Contact No"])
doctors_df.head(10)  # Show first 10 rows
doctors_df.to_csv('doctors.csv')
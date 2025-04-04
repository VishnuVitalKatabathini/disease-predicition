import streamlit as st
import prediction
import pandas as pd
import con_db

# Load the ML model
model = prediction.rnd_forest

# App Title
st.title("AI Disease Predictor")
st.write("Select up to 3 symptoms to predict the most likely disease.")

# Load symptoms
df = pd.read_csv('archive/Symptom-severity.csv')
unique_symptoms = df["Symptom"].unique()

# Input: Symptoms
symptoms = st.multiselect("Choose up to 3 symptoms:", unique_symptoms, max_selections=3)

# Prediction
if st.button("Predict"):
    if len(symptoms) == 0:
        st.warning("Please select at least one symptom.")
    else:
        # Ensure exactly 3 symptoms are passed (fill missing with empty strings)
        while len(symptoms) < 3:
            symptoms.append("")

        result = prediction.predd(
            model,
            symptoms[0], symptoms[1], symptoms[2],
            "", "", "", "", "", "", "", "", "", "", "", "", ""
        )

        disease_predicted = result[0]
        st.success(f"Disease Predicted: {disease_predicted}")
        st.info(f"Description: {result[1]}")
        st.warning(f"Precautions: {result[2]}")

        # Store prediction in session state
        st.session_state['predicted_disease'] = disease_predicted

# Doctor Consultation
if 'predicted_disease' in st.session_state:
    if st.button("Consult Doctor"):
        con = con_db.ConnectDB()
        doctors = con.search(st.session_state['predicted_disease'])

        if doctors:
            st.subheader("Available Doctor(s):")
            for doc in doctors:
                st.write(f"**Name:** {doc[0]}  \n**Contact:** {doc[1]}")
        else:
            st.error("No doctor found for this disease.")

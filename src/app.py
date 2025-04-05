import streamlit as st
import prediction
import pandas as pd
import con_db

# Dummy function for disease prediction (replace with ML model later)
# def predict_disease(symptoms):
#     pass
    # Just a dummy example, replace with a real model
#load the model
model=prediction.rnd_forest

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio("Navigate", [ "Predict Disease"])



# Disease Prediction Page
if menu == "Predict Disease":
    st.title("Disease Prediction")
    
    # Symptoms input
    df=pd.read_csv('archive/Symptom-severity.csv')
    unique_diseases = df["Symptom"].unique()
    symptoms = st.multiselect(
        "Select  symptoms below:",
        unique_diseases
    )

    # Predict Button
    if st.button("Predict"):
        print(symptoms)
        length=len(symptoms)
        print(length)
        rem=17-len(symptoms)
        print('remaining length:',rem)
        for i in range(rem):
            symptoms.append(0)
        print('final length',len(symptoms))

        print(type(symptoms))
        if symptoms:
            result = prediction.predd(model, symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4], symptoms[5], symptoms[6], symptoms[7],symptoms[8], symptoms[9], symptoms[10], symptoms[11], symptoms[12], symptoms[13], symptoms[14], symptoms[15], symptoms[16])
        
            disease_predicted = result[0]
            st.success(f"Disease Predicted: {disease_predicted}")
            st.success(f"disease description:{result[1]}")
            st.success(f"disease precautions:{result[2]}")

        # Store the disease for use when consulting a doctor
            st.session_state['predicted_disease'] = disease_predicted

        else:
            st.warning("Please select at least one symptom.")


# Show Consult Doctor button only if disease is predicted
    if 'predicted_disease' in st.session_state:
        if st.button("Consult Doctor"):
            # consult_doctor = con_db.ConnectDB.search(st.session_state['predicted_disease'])
            con_db = con_db.ConnectDB()  # Create an instance
            consult_doctor = con_db.search(st.session_state['predicted_disease'])


            if consult_doctor:
                st.subheader("Available Doctor(s):")
                for doc in consult_doctor:
                    st.write(f"**Name:** {doc[0]}  \n**Contact:** {doc[1]}")
            else:
                st.warning("No doctor found for this disease.")



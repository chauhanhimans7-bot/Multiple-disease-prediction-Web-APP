
"""
Created on Tue Feb 10 16:26:29 2026

@author: Yuri
"""
import numpy
import streamlit as st
from streamlit_option_menu import option_menu
import pickle

    
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

path = "C:/Users/Yuri/Desktop/multiple disease prediction system/saved model/diabetes_model.sav"
diabetes_model =pickle.load(open(path,'rb'))
heart_disease_model = pickle.load(open("C:/Users/Yuri/Desktop/multiple disease prediction system/saved model/heart_disease.sav",'rb'))
parkinsons_model = pickle.load(open("C:/Users/Yuri/Desktop/multiple disease prediction system/saved model/parkinsons_model.sav",'rb'))
st.markdown("""
    <style>
    /* 1. Style the button itself */
    div.stButton > button:first-child {
        background-color: #0099ff; /* Blue color */
        color: white;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease-in-out; /* This makes it animated */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* 2. Style the hover effect (when mouse is over the button) */
    div.stButton > button:first-child:hover {
        background-color: #0077cc; /* Darker blue */
        color: #fffd;
        transform: translateY(-2px); /* Moves the button up slightly */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }

    /* 3. Style the click effect */
    div.stButton > button:first-child:active {
        transform: translateY(0px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("MULTIPLE DISEASE PREDICTION SYSTEMMM",
                           ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],default_index= 0,icons = ["activity","heart-pulse","person-plus-fill"])
    
if (selected == "Diabetes Prediction"):
    st.title("Diabetes Prediction using ML")
    
    # Use columns for a cleaner layout
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        BloodPressure = st.text_input("Blood Pressure value")
        Insulin = st.text_input('Insulin Level')
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Glucose = st.text_input("Glucose level")
        SkinThickness = st.text_input("Skin Thickness value")
        BMI = st.text_input("BMI value")
        Age = st.text_input("Age of the person")

    # Initialize diagnosis as None or empty
    diab_diagnosis = ""

    if st.button("Diabetes Test Result"):
        # 1. Create a list of all inputs
        user_inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        # 2. Check if any input is empty or just whitespace
        if any(x.strip() == "" for x in user_inputs):
            st.error("Please enter all details from the report.")
        else:
            # 3. If all fields are filled, convert and predict
            try:
                numeric_input = [float(x) for x in user_inputs]
                prediction = diabetes_model.predict([numeric_input])

                if prediction[0] == 1:
                    diab_diagnosis = "The Person is Diabetic"
                else:
                    diab_diagnosis = "The Person is not Diabetic"
                
                st.success(diab_diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values.")
                                   
                                
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')

    # Organize into columns for a better look
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Gender (1=M, 0=F)')
        cp = st.text_input('Chest Pain types (0-3)')
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral (mg/dl)')
        fbs = st.text_input('Fasting Blood Sugar > 120 (1=T, 0=F)')
        restecg = st.text_input('Resting ECG results (0-2)')
        thalach = st.text_input('Max Heart Rate')

    with col3:
        exang = st.text_input('Exercise Angina (1=Y, 0=N)')
        oldpeak = st.text_input('ST depression')
        slope = st.text_input('ST segment slope (0-2)')
        ca = st.text_input('Major vessels (0-3)')
        
    thal = st.text_input('Thalassemia (0=normal; 1=fixed; 2=reversible)')

    # Prediction Logic
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        # 1. Collect all inputs into a list
        user_inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        # 2. Check if any field is empty (strip removes whitespace)
        if any(x.strip() == "" for x in user_inputs):
            st.error("Please enter all the report data.")
        else:
            try:
                # 3. Convert all inputs to float for the model
                numeric_input = [float(x) for x in user_inputs]
                
                # 4. Get the prediction
                prediction = heart_disease_model.predict([numeric_input])

                if (prediction[0] == 1):
                    heart_diagnosis = 'The person is predicted to have heart disease'
                else:
                    heart_diagnosis = 'The person is predicted to not have heart disease'
                
                # Show the result only after successful calculation
                st.success(heart_diagnosis)
                
            except ValueError:
                st.error("Please enter valid numeric values in all fields.")      


if (selected == "Parkinsons Prediction"):

    st.title("Parkinson's Disease Prediction using ML")

    # Creating four columns to handle the 22 inputs efficiently
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        fhi = st.text_input('MDVP:Fhi(Hz)')
        flo = st.text_input('MDVP:Flo(Hz)')
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        rap = st.text_input('MDVP:RAP')

    with col2:
        ppq = st.text_input('MDVP:PPQ')
        ddp = st.text_input('Jitter:DDP')
        shimmer = st.text_input('MDVP:Shimmer')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
        apq3 = st.text_input('Shimmer:APQ3')
        apq5 = st.text_input('Shimmer:APQ5') # Corrected variable name from your snippet

    with col3:
        apq = st.text_input('MDVP:APQ')
        dda = st.text_input('Shimmer:DDA')
        nhr = st.text_input('NHR')
        hnr = st.text_input('HNR')
        rpde = st.text_input('RPDE')
        dfa = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        d2 = st.text_input('D2')
        ppe = st.text_input('PPE')

    # Initialize diagnosis
    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        # 1. Collect all inputs
        user_inputs = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                       shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                       rpde, dfa, spread1, spread2, d2, ppe]
        
        # 2. Check for empty fields
        if any(x.strip() == "" for x in user_inputs):
            st.warning("Please enter all the report data before predicting.")
        else:
            try:
                # 3. Convert all to float
                numeric_input = [float(x) for x in user_inputs]

                # 4. Predict
                prediction = parkinsons_model.predict([numeric_input])

                if (prediction[0] == 1):
                    parkinsons_diagnosis = "The person is predicted to have Parkinson's disease"
                    st.error(parkinsons_diagnosis)
                else:
                    parkinsons_diagnosis = "The person is predicted to not have Parkinson's disease"
                    st.success(parkinsons_diagnosis)
            
            except ValueError:
                st.error("Please enter valid numeric values. Make sure there are no letters in the fields.")                             
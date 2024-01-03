import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
import pickle
import streamlit as st

# Load the dataset
df = pd.read_csv("kidney_disease.csv")

# Preprocessing
data = df.loc[:, ["bgr", "rc", "wc", "classification"]]
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

x[x == "\t?"] = np.nan
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 0:3])
x[:, 0:3] = imputer.transform(x[:, 0:3])

le = LabelEncoder()
y = le.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Train the CatBoostClassifier
cat = CatBoostClassifier(iterations=10)
cat.fit(x_train, y_train)

# Save the model using pickle
with open("cat_model.pkl", "wb") as file:
    pickle.dump((cat, imputer, le), file)

# Streamlit app
st.title("Kidney Disease Prediction App")

# Input form
bgr = st.text_input("Blood Glucose Random (bgr)")
rc = st.text_input("Red Blood Cell Count (rc)")
wc = st.text_input("White Blood Cell Count (wc)")

if st.button("Predict"):
    try:
        bgr_val = float(bgr)
        rc_val = float(rc)
        wc_val = float(wc)

        input_data = [[bgr_val, rc_val, wc_val]]

        # Load the model, imputer, and label encoder
        with open("cat_model.pkl", "rb") as file:
            loaded_model, loaded_imputer, loaded_le = pickle.load(file)

        # Impute missing values
        input_data_imputed = loaded_imputer.transform(input_data)

        # Scale features using StandardScaler
        scaler = StandardScaler()
        input_data_scaled = scaler.fit_transform(input_data_imputed)

        # Make prediction on user input
        prediction = loaded_model.predict(input_data_scaled)

        # Display result
        if prediction == 0:
            st.write("The Person is suffering from Chronic disease")
        else:
            st.write("No Chronic diseases")

    except ValueError:
        st.write("Please enter valid numeric values.")

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

model = pickle.load(open('model.pkl', 'rb'))

def welcome():
    return "Welcome All"

def predict(LIMIT_BAL, PAY_1, PAY_2, PAY_3, PAY_4,PAY_5, PAY_6):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: LIMIT_BAL
        in: query
        type: number
        required: true
      - name: PAY_1
        in: query
        type: number
        required: true
      - name: PAY_2
        in: query
        type: number
        required: true
      - name: PAY_3
        in: query
        type: number
        required: true
      - name: PAY_4
        in: query
        type: number
        required: true
      - name: PAY_5
        in: query
        type: number
        required: true
      - name: PAY_6
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    prediction=model.predict([[LIMIT_BAL, PAY_1, PAY_2, PAY_3, PAY_4,PAY_5, PAY_6]])
    print(prediction)
    output = round(prediction[0], 1)
    if output>0.5:
        return " Fraud " 
    else:
        return " Not Fraud " 


def main():
    st.title("Credit Card Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit Fraud ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    LIMIT_BAL = st.text_input("LIMIT_BAL","Type Here")
    PAY_1 = st.text_input("PAY_1","Type Here")
    PAY_2 = st.text_input("PAY_2","Type Here")
    PAY_3 = st.text_input("PAY_3","Type Here")
    PAY_4 = st.text_input("PAY_4","Type Here")
    PAY_5 = st.text_input("PAY_5","Type Here")
    PAY_6 = st.text_input("PAY_6","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(LIMIT_BAL,PAY_1, PAY_2,PAY_3, PAY_4,PAY_5, PAY_6)
    st.success('Person is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
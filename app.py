# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:34:31 2023

@author: arath
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from joblib import dump, load

classifier = load("Loan.joblib")

def main():
    st.title('This is Loan Approval Prediction')
    st.sidebar.title('This app predicts if your Loan is Approved or no')
    Married = st.sidebar.selectbox('Enter your Marital Status(0 for No, 1 for Yes): ',(0,1))
    Gender=st.sidebar.selectbox("enter your gender",(0,1))
    Dependents=st.sidebar.number_input('Enter number of dependents: ')    
    Education=st.sidebar.selectbox('Enter Education status(0 for graduates 1 for non graduates): ',(0,1))    
    Self_Employed=st.sidebar.selectbox('are you Self Employed (1 for yes 0 for no): ',(0,1))
    ApplicantIncome=st.sidebar.number_input('Enter your income ')  
    CoapplicantIncome=st.sidebar.number_input('Enter coapplicants income if applicable ')
    LoanAmount=st.sidebar.number_input('Enter Loan amount ')
    Loan_Amount_Term=st.sidebar.number_input('Enter term in days ')
    Credit_History=st.sidebar.selectbox('enter credit history 0 or 1',(0,1))
    Property_Area=st.sidebar.selectbox('enter your area(0 for rural, 1 for semi-urban, 2 for urban',(0,1,2))
    if st.sidebar.button('Predict'):
        predictions = classifier.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
        st.write(predictions)
        if predictions==1:
            st.title('Loan approved!!')
        else:
            st.title('Not Approved')
if __name__ =='__main__':
    main()
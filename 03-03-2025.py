import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
st.title('Model Deployement: Logistic Regression')
st.sidebar.header('USer Input ')




def user_input_features():

    CLMSEX = st.sidebar.selectbox('Gender',('1','0'))

    CLMINSUR = st.sidebar.selectbox('Insurance',('1','0'))

    SEATBELT = st.sidebar.selectbox('SeatBelt',('1','0'))

    CLMAGE = st.sidebar.number_input("Insert the Age")

    LOSS = st.sidebar.number_input("Insert Loss")

    data = {'CLMSEX':CLMSEX,

            'CLMINSUR':CLMINSUR,

            'SEATBELT':SEATBELT,

            'CLMAGE':CLMAGE,

            'LOSS':LOSS}


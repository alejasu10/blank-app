import streamlit as st
import pandas as pd

def load_datos():
    df=pd.read_csv("")
    return df

df= load_datos()
st.write(df)
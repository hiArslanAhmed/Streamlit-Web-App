# Import Necsaary Library
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Webapp Title
st.markdown(''' 
#  **Exploratory Data Analysis Web Application**
This application is developed by Arslan Ahmed''')

with st.sidebar.header("Upload you file(.csv)"):
    uploaded_file = st.sidebar.file_uploader("upload your file", type =["csv"])

    df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Example csv file]('http://winterolympicsmedals.com/medals.csv')")


# Profiling report for pandas
if uploaded_file is not None:
    st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("**Input DataFrame**")
    st.write(df)
    st.write("---")
    st.header("**profiling report with pandas**")
    st_profile_report(pr)

else:
    st.header("Awaiting for csv file")
    if st.button("press to use Example Data"):
        
    
    #  Example Dataset
        st.cache_data
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5 ),
                         columns = ["A", "B", "C", "D", "E"])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header("**Input DataFrame**")
        st.write(df)
        st.write("---")
        st.header("**profiling report with pandas**")
        st_profile_report(pr)
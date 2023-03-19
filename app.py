import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# make a container

header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kashti ke app")
    st.text("in this project we will work on kashti DataFrame")

with data_set:
    st.header("Kashti doob gaye, Haww!")
    st.text("We will work with titanic dataset")
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head(10))

    st.subheader("Saambha Arey oooo Sambha kitnay Aadmi they")
    st.bar_chart(df["sex"].value_counts())

    st.subheader("Class k hisaab se farq")
    st.bar_chart(df["class"].value_counts())
    # Bar plot 
    st.bar_chart(df["age"].sample(30)) # or use head function



with features:
    st.header("These are our app features")
    st.text("awaen bht saaray features add krtay hain asaan he hain")
    st.markdown("**Features** 1: This will tell us pta nai kya")


with model_training:
    st.header("kashti walu ka kya bna?  Modle Training")
    st.text("iss me ham apne parameteres ko kam ya ziada kre gey")
    # Making columns
    input, display = st.columns(2)

    # pehlay column me apkay selection column hu
    max_depth = input.slider("How many people do you know?", min_value=10, max_value=100, step=5,value=20)
    # n_estimators
    n_estimators = input.selectbox("How many tress in there a Random Forest", options=[50,100,200,300,"No Input"])

    # Input Features from user
    input_features = input.text_input("Which features we should use?")

    #Mashine Learning Models
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    # Defining X and Y
    X = df[[input_features]]
    y = [["fare"]]

    # fit our model
    model.fit(X,y)
    pred = model.predict(y)

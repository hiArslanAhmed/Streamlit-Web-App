
# import necessary libraries
import plotly.express as px
import streamlit as st
import pandas as pd

# Import Dataset
st.title("Make an interactive plots in Plotly Express")

st.header("Name of dataset _**Iris**_ Dataset")
df = px.data.iris()
st.write(df)


st.header("Name of the Columns")
st.write(df.columns)


# Summary Statitics
st.header("Summary statistics of DataFrame")
st.write(df.describe())




# Create a Streamlit selectbox to choose which variables to display
x_variable = st.sidebar.selectbox("X-axis variable", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
y_variable = st.sidebar.selectbox("Y-axis variable", ["sepal_length", "sepal_width", "petal_length", "petal_width"])

# Create the violin plot with colors based on the species
fig = px.violin(df, x="species", y=y_variable, color="species", box=True,
                points="all", hover_data=df.columns, title=f"Iris Dataset {y_variable} by Species")

# Show the plot in Streamlit
st.plotly_chart(fig)


# Show the plot in Streamlit
st.plotly_chart(fig)
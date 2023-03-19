
# import necessary libraries
import plotly.express as px
import streamlit as st
import pandas as pd

# Import Dataset
st.title("Make an interactive plots in Plotly Express")

st.header("Name of dataset GapMinder Dataset")
df = px.data.gapminder()
st.write(df)


st.header("Name of the Columns")
st.write(df.columns)


# Summary Statitics
st.header("Summary statistics of DataFrame")
st.write(df.describe())


# Data Management
year_option = df["year"].unique().tolist()
year = st.selectbox("Which year should we plot?", year_option, 0)
# df = df[df["year"] == year]
# plotting 
fig = px.scatter(df, x = "gdpPercap",y = "lifeExp", size = "pop",
                 color = "country", hover_name = "country", 
                  log_x = True, size_max = 55, range_x = [100,100000], range_y = [20,90],
                  animation_frame="year", animation_group="country")

st.write(fig)
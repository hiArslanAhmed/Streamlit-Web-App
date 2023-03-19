import streamlit as st
import seaborn as sns
st.header("This is video is brought to you by #Arslan_Javed")
st.text("Streamlit is Amazing")

st.header("Hello Mr Usama_Karim")
st.text("kese lgi aapko streamlit ")

import seaborn as sns
df = sns.load_dataset("iris")
st.write(df[["sepal_length", "petal_length", "species"]].head(10))

st.header("Making a lineplot")
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Select the data to plot
x = iris["sepal_length"]
y = iris["petal_length"]

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set plot title and axis labels
ax.set_title('Iris Dataset')
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Petal Length')

# Display plot in Streamlit app
st.pyplot(fig)



st.header("Making a  Bar Chart")

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Group the data by species and calculate the mean of each feature
iris_mean = iris.groupby("species").mean()

# Create a bar chart
fig, ax = plt.subplots()
iris_mean.plot(kind="bar", ax=ax)

# Set plot title and axis labels
ax.set_title("Average Iris Measurements by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Measurement")

# Display plot in Streamlit app
st.pyplot(fig)


st.line_chart(df["sepal_length"])



st.header("Make your Own Profile")

import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Arslan", page_icon=":Arslan:")

# Display profile picture
profile_picture = st.file_uploader("pic.jpg")
if profile_picture is not None:
    st.image(profile_picture, use_column_width=True)

# Display profile information
st.title("Arslan Ahmed")
email = st.text_input("Email", "hi33arslan@gmail.com")
location = st.text_input("Location", "Pakistan,Gujranwala")

# Display charts and widgets
st.header("My Interests")

# Pie chart of interests
interests = {"Reading": 20, "Travel": 30, "Cooking": 25, "Fitness": 25}
fig1, ax1 = plt.subplots()
ax1.pie(list(interests.values()), labels=list(interests.keys()), autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Bar chart of book genres
book_genres = ['Mystery', 'Romance', 'Science Fiction', 'Thriller', 'Fantasy']
books_read = [12, 8, 5, 10, 6]
fig2, ax2 = plt.subplots()
ax2.bar(book_genres, books_read)
ax2.set_title("Books Read by Genre")
ax2.set_xlabel("Genre")
ax2.set_ylabel("Number of Books")
st.pyplot(fig2)

# Display widget to select favorite book
st.header("My Favorite Book")
book_options = ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice']
favorite_book = st.selectbox("Select your favorite book", book_options)
st.write("Your favorite book is:", "History of Islam")



# import necessary libraries
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Create logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Calculate accuracy of model
accuracy = accuracy_score(y_test, y_pred)

# Create Streamlit app
st.title('Iris dataset classification using Logistic Regression')
st.write(f'Accuracy: {accuracy:.2f}')

# Add user input fields for iris features
sepal_length = st.number_input('Sepal length', value=5.0, step=0.1)
sepal_width = st.number_input('Sepal width', value=3.5, step=0.1)
petal_length = st.number_input('Petal length', value=1.4, step=0.1)
petal_width = st.number_input('Petal width', value=0.2, step=0.1)

# Make prediction on user input
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)[0]
predicted_class_name = class_names[prediction]

# Show predicted class to user
st.write(f'Predicted class: {predicted_class_name}')




# prompt: Write me a code to explaine 80% off all python data scince concepsts with comments and examples. Assume that i know very basic stuff. You can make different topics in diferent code blocks

# 80% of Python Data Science Concepts (Simplified)

# 1. NumPy (Numerical Python): Efficient arrays and matrices

import numpy as np

# Creating a NumPy array
my_array = np.array([1, 2, 3, 4, 5])
print("My NumPy array:", my_array)


# Array operations
print("Adding 2 to each element:", my_array + 2)
print("Multiplying array by 2:", my_array * 2)
# Array slicing (accessing parts of the array)
print("Elements 2 to 4:", my_array[1:4])


# 2. Pandas (Data Analysis): DataFrames for structured data

import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}

# Creating a DataFrame
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Accessing data
print("\nFirst two rows:\n", df.head(2)) # first two rows
print("\nColumn 'Name':\n", df['Name'])  # Access a column


#Filtering data
filtered_df = df[df['Age'] > 25]
print("\nPeople older than 25:\n", filtered_df)

# 3. Matplotlib (Visualization): Creating plots and charts

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Creating a simple line plot
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show() #This will show the plot in colab


# 4. Scikit-learn (Machine Learning): Algorithms for predictions

from sklearn.linear_model import LinearRegression

# Sample data (simple linear regression)
x = np.array([[1], [2], [3]])
y = np.array([2, 4, 5])


# Create and fit the model
model = LinearRegression()
model.fit(x,y)

# Make predictions
print("\nPrediction for x=4:", model.predict([[4]]))


# 5. Basic Statistics (Descriptive statistics)

#Mean calculation
numbers = np.array([1,2,3,4,5])
print(f"\nMean : {np.mean(numbers)}")

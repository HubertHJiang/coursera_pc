# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:02:14 2024

@author: 27519
"""

# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns


df=pd.read_csv('dataset_part_2.csv')
df.head(5)


sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

# A function to Extract years from the date 
year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
df.head()

features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

sns.catplot(x="PayloadMass", y="LaunchSite", hue='Class', data=df)

# Group by 'Orbit' and calculate the mean of 'Class'
success_rate = df.groupby('Orbit')['Class'].mean()

# Create a bar chart
success_rate.plot(kind='bar', color='skyblue')

# Add labels and title
plt.xlabel('Orbit')
plt.ylabel('Success Rate')
plt.title('Success Rate by Orbit')

# Show the plot
plt.show()


sns.scatterplot(data=df, x="FlightNumber", y="Orbit", hue="Class")

# Add labels and title
plt.xlabel('Flight Number')
plt.ylabel('Orbit')
plt.title('Scatter Plot of Flight Number vs Orbit')

# Show the legend
plt.legend(title='Class')

# Show the plot
plt.show()

sns.scatterplot(data=df, x="PayloadMass", y="Orbit", hue="Class")

# Add labels and title
plt.xlabel('Payload Mass')
plt.ylabel('Orbit')
plt.title('Scatter Plot of Payload Mass vs Orbit')

# Show the legend
plt.legend(title='Class')

# Show the plot
plt.show()

df['Year'] = df['Date'].apply(lambda x: x.split("-")[0])

# Calculate the average success rate for each year
average_success_rate = df.groupby('Year')['Class'].mean()

# Plot a line chart
plt.figure(figsize=(10, 6))
plt.plot(average_success_rate.index, average_success_rate.values, marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Average Success Rate')
plt.title('Launch Success Trend by Year')

# Show the grid
plt.grid(True)

# Show the plot
plt.show()






















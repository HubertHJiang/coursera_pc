# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:56:08 2024

@author: 27519
"""

# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)

df.isnull().sum()/len(df)*100

df.dtypes

# Assuming your DataFrame is named 'df'
launch_site_counts = df['LaunchSite'].value_counts()
print(launch_site_counts)

orbit_counts = df['Orbit'].value_counts()
print(orbit_counts)

landing_outcomes = df['Outcome'].value_counts()

for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes

bad_outcome = {'failed', 'exploded', 'crashed'}  # Example set of bad outcomes
landing_class = [1 if outcome not in bad_outcome else 0 for outcome in df['Outcome']]

df['Class']=landing_class
df[['Class']].head(8)
df.head(5)

df["Class"].mean()
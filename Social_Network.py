#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv("Social_Network_ads.csv")
x = dataset.iloc[:,0:3]. values
y = dataset.iloc[:,3:4].values


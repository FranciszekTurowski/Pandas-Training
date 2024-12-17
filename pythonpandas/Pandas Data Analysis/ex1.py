import pandas as pd
import matplotlib.pyplot as plt


""" Task 1: Load the data and display basic information about it."""
    
data = pd.read_csv('pokemon.csv')
print("TASK 1")
print(data.info())
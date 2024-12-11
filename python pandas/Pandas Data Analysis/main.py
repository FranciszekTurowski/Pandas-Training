import pandas as pd
import matplotlib.pyplot as plt

def main():
    """ Task 1: Load the data and display basic information about it."""
    
    data = pd.read_csv('telecom_churn.csv')
    print("TASK 1")
    print(data.info())
    
    """ Task 2: Displays the first 5 rows of the dataset. """
    
    print("TASK 2")
    print(data.head())
    
    """ Task 3: Display basic statistics."""
    
    print("TASK 3")
    print(data.describe())
    
    """ Task 4: Count the number of churned customers."""
    
    print("TASK 4")
    print(data['Churn'].value_counts())
    
    """ Task 5: Calculate the average daily minutes for all customers."""
    
    print("TASK 5")
    print(data['Total day minutes'].mean())
    
    """ Task 6: Calculate the total revenue from daily services."""
    
    print("TASK 6")
    print(data['Total day charge'].sum())
    
    """ Task 7: Calculate the percentage of customers with an international plan."""
    
    print("TASK 7")
    print((data['International plan'] == 'Yes').mean() * 100)
    
    """ Task 8: Calculate the average number of service calls."""
    
    print("TASK 8")
    print(data['Customer service calls'].mean())
    
    """ Task 9: Display the correlation matrix for numerical data."""
    
    print("TASK 9")
    print(data.select_dtypes(include='number'))
    
    """ Task 10: Plot the distribution of churned customers."""
    
    print("TASK 10")
    data['Churn'].value_counts().plot(kind='bar')
    plt.title('Rozkład klientów - Churn')
    plt.xlabel('Churn')
    plt.ylabel('Liczba klientów')
    plt.show()
    
    """ Task 11: Calculate the average charge per call."""
    
    print("TASK 11")
    print((data['Total day charge'] / data['Total day calls']).mean())
    
    """ Task 12: Find the customer with the highest daily usage."""
    
    print("TASK 12")
    print(data.loc[data['Total day minutes'].idxmax()])
    
    """ Task 13: Filter customers with a voicemail plan."""
    
    print("TASK 13")
    print(data[data['Voice mail plan'] == 'Yes'])
    
    """ Task 14: Calculate the average night minutes for churned customers."""
    
    print("TASK 14")
    churned = data[data['Churn'] == True]
    print(churned['Total night minutes'].mean())
    
    """ Task 15: Count the number of unique area codes."""
 
    print("TASK 15")
    print(data['Area code'].nunique())
    
    """ Task 16: Plot the distribution of total day minutes."""
    
    print("TASK 16")
    
    """ Task 17: Find customers with more than 5 service calls."""
    
    print("TASK 17")
    
    """ Task 18: Calculate the churn rate as a percentage."""
    
    print("TASK 18")
    
    """ Task 19: Calculate the average international minutes per customer."""
    
    print("TASK 19")
    
    """ Task 20: Find the top 3 states with the highest churn rate."""
    
    print("TASK 20")
    
    """ Task 21: Plot the average daily charge by state."""
    
    print("TASK 21")
    
    """ Task 22: Identify high-value customers based on spending and activity."""
    
    print("TASK 22")
    
    """ Task 23: Analyze service usage patterns."""
    
    print("TASK 23")
    
    """ Task 24: Identify at-risk customers based on the number of service calls."""
    
    print("TASK 24")
    
    """ Task 25: Calculate the average total charge for churned customers."""
    
    print("TASK 25")
    
    """ Task 26: Calculate the average total charge for loyal customers."""
    
    print("TASK 26")
    
    """ Task 27: Calculate the average total charge for customers with an international plan."""
    
    print("TASK 27")
    
    """ Task 28: Calculate the average total charge for customers without an international plan."""
    
    print("TASK 28")
    
    """ Task 29: Calculate the average total charge for customers with voicemail."""
    
    print("TASK 29")
    
    """ Task 30: Find the customer with the highest total charge."""
    
    print("TASK 30")

if __name__ == "__main__":
   main()
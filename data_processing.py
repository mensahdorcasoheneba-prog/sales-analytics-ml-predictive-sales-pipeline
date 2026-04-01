import pandas as pd
import numpy as np
 
class SalesDataProcessor:
    def __init__(self, filename):
        # Load data immediately upon creation
        self.df = pd.read_csv(filename)
 
    def clean_data(self):
        # STEP 1: Remove anomalies (Unit_Price > 10,000)
        # keep rows where Unit_Price <= 10000
        self.df = self.df[np.where(self.df['Unit_Price'] <= 10000, True, False)]
 
processor = SalesDataProcessor(r"C:\Users\USER\Desktop\sales_data\GLOBAL SALES DATA.csv")
print(processor.df)
 
#check data type
#print(processor.df.dtypes)
# clean data and show head
#processor.clean_data()
#print(processor.df.head())
 
#high_price_rows = processor.df[processor.df['Unit_Price'] > 10000]
#print(high_price_rows)
 
 #Create a new column called Transaction_Type to handle refund
#processor.df['Transaction_Type'] = np.where(processor.df['Quantity'] < 0,'Refund', 'Purchase')
#print(processor.df)
# check for refunded transaction
#Refund = processor.df[processor.df['Transaction_Type'] == 'Refund' ]
#print(Refund)
 
# fix missing data in payment_method
#processor.df['Payment_Method'] = processor.df['Payment_Method'].fillna("Unknown")
 
# CHECK FOR UNKOWN and add .shape[0] to count the rows of unknown
#Unknown = processor.df[processor.df['Payment_Method'] == 'Unknown']
#print(Unknown)
 
#Unknown = processor.df[processor.df['Payment_Method'] == 'Unknown'].shape[0]
#print(Unknown)
 
# question 3 Add a method called calculate_category_volatility
       
# 1. Create a column Total_Amount (Quantity * Unit_Price)
# Multiply two columns to get the total revenue per row
processor.df['Total_Amount'] = processor.df['Quantity'] * processor.df['Unit_Price']
 
# Run this to see the new column added at the end
print(processor.df[['Quantity', 'Unit_Price', 'Total_Amount']])
 
# Group by Category and find the Standard Deviation
#volatility_results = processor.df.groupby('Category')['Total_Amount'].std()
 
# Run this to see the volatility score for every category
#print(volatility_results)
 
# .idxmax() picks the category name associated with the highest number
#most_volatile = volatility_results.idxmax()
 
# Run this to get your final answer for the report
#print(f"The most volatile category is: {most_volatile}")
 
 
#QUESTION 4: Trend Visualization ---
 
import matplotlib.pyplot as plt
 
 # THE FIX: Convert text to actual Date objects before setting the index
 
processor.df['Date'] = pd.to_datetime(processor.df['Date'])
 
# Now set the index and resample
monthly_sales = processor.df.set_index('Date')['Total_Amount'].resample('ME').sum()
 
# Print the results
print("\n--- Processed Monthly Sales Data ---")
print(monthly_sales)
 
# Create the Figure
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='blue', linewidth=2)
 
# Add labels
plt.title('Monthly Sales Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True, linestyle='--', alpha=0.7)
 
# Save and then explicitly SHOW the window
plt.savefig('sales_trend.png')
print("\nSuccess! Opening the visualization window...")
plt.show()

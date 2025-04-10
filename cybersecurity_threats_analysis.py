#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r'Datasets\Global_Cybersecurity_Threats_2015-2024.csv')

# Financial loss analysis
financial_loss_by_year = data.groupby('Year')[["Financial Loss (in Million $)"]].sum().sort_values(by='Financial Loss (in Million $)', ascending=False)
financial_loss_by_year_avg = data.groupby('Year')[["Financial Loss (in Million $)"]].mean().sort_values(by='Financial Loss (in Million $)', ascending=False)
financial_loss_by_year_max = data.groupby('Year')[["Financial Loss (in Million $)"]].max().sort_values(by='Year', ascending=False)
financial_loss_by_year_min = data.groupby('Year')[["Financial Loss (in Million $)"]].min().sort_values(by='Year', ascending=False)
'''
print(financial_loss_by_year)
print(financial_loss_by_year_avg)
print(financial_loss_by_year_max)
print(financial_loss_by_year_min)
'''

# Define count_atacks()
def count_atacks(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


attack_type_count = count_atacks(data, 'Attack Type')
target_industry_count = count_atacks(data, 'Target Industry')


print(attack_type_count)
print(target_industry_count)
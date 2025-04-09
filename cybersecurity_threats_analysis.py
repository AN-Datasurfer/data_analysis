#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r'Datasets\Global_Cybersecurity_Threats_2015-2024.csv')

# Financial loss analysis
financial_loss_by_year = data.groupby('Year')[["Financial Loss (in Million $)"]].sum().sort_values(by='Financial Loss (in Million $)', ascending=False)
avg_financial_loss_by_year = data.groupby('Year')[["Financial Loss (in Million $)"]].mean().sort_values(by='Financial Loss (in Million $)', ascending=False)

print(financial_loss_by_year)
print(avg_financial_loss_by_year)


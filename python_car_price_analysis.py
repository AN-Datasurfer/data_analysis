import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt

car_data = pd.read_csv(r'Datasets/car_price_dataset.csv')
car_data_audi = car_data[car_data['Brand'] == 'Audi']

#variables
analised_mileage = 10000

car_data_audi_milage = car_data_audi[car_data_audi['Mileage'] < analised_mileage]

#separated_columns_Pandas_DataFrame
column_brand = car_data[['Brand']]
column_model = car_data[['Model']]
column_year = car_data[['Year']]
column_engine_size = car_data[['Engine_Size']]
column_fuel_type = car_data[['Fuel_Type']]
column_transmition = car_data[['Transmission']]
column_doors = car_data[['Doors']]

#separated_columns_Pandas_Series
column_owner_count = car_data['Owner_Count']
column_price = car_data['Price']
column_mileage = car_data['Mileage']


#separated_columns_Pandas_Series_Audi
column_owner_count_audi = car_data_audi_milage['Owner_Count']
column_price_audi = car_data_audi_milage['Price']
column_mileage_audi = car_data_audi_milage['Mileage']
column_model_audi = car_data_audi_milage['Model']

#creating arrays 
np_column_price = np.array(column_price)
np_column_price_to_owner_count = np.array(column_price, column_owner_count)

#price_descriptive_statistics
price_sum = np_column_price.sum()    # Sum of elements
price_mean = np_column_price.mean()  # Mean of elements
price_min = np_column_price.min()    # Minimum value
price_max = np_column_price.max()    # Maximum value
price_std = np_column_price.std()    # Standard deviation

#Variables for viz
x = column_price_audi
y = column_owner_count_audi

#Visualization of data
plt.scatter(x ,y, s=10,cmap='coolwarm',zorder=1)

plt.yscale('linear')      # Options: 'linear', 'log', 'symlog', 'logit'
plt.xscale('linear')      # Options: 'linear', 'log', 'symlog', 'logit'

plt.xlabel("Milage", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.title("Audi price to mileage", fontsize=14)

plt.show()



#outputs
print('Standard deviation of car price is: ', round(price_std))
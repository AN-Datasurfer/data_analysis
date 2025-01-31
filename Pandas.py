import pandas as pd
import numpy as np
import math as mt
car_data = pd.read_csv(r'car_price_dataset.csv')

engine_size_subset = car_data[['Engine_Size']]


#separated_columns
column_brand = car_data[['Brand']]
column_model = car_data[['Model']]
column_year = car_data[['Year']]
column_engine_size = car_data[['Engine_Size']]
column_fuel_type = car_data[['Fuel_Type']]
column_transmition = car_data[['Transmission']]
column_mileage = car_data[['Mileage']]
column_doors = car_data[['Doors']]
column_owner_count = car_data[['Owner_Count']]
column_price = car_data[['Price']]

#creating arrays 
np_column_price = np.array(column_price)


#print(car_data.info)
#print(engine_size_subset.info)

#print(car_data.loc[4])

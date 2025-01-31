import pandas as pd
car_data = pd.read_csv(r'car_price_dataset.csv')

engine_size_subset = car_data[['Engine_Size']]

#print(car_data.info)
print(engine_size_subset.info)

print(car_data.loc[4])
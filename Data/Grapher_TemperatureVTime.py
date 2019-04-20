### Temperature vs. time

import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingTemperatureGradient_Trial01_20190326.xls", delimiter = "\t")

data = pp.remove_notes(data)

print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
first_column = pd.to_numeric(data.iloc[:,0]) #Day fraction
print(first_column)
third_column = pd.to_numeric(data.iloc[:,2]) #Effluent temperature
print(third_column)
fourth_column = pd.to_numeric(data.iloc[:,3]) #Influent temperature
print(fourth_column)
elapsed_time = (np.array(first_column)-first_column[0])*24*60*60

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (C)")
plt.plot(elapsed_time, third_column, fourth_column,'o' ,color="blue")

# plt.savefig("Images/test.png")

import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingPressure_20190418.xls", delimiter = "\t")

data = pp.remove_notes(data)

print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
first_column = pd.to_numeric(data.iloc[:,0])
print(first_column)
fourth_column = pd.to_numeric(data.iloc[:,3])
print(fourth_column)
elapsed_time = (np.array(first_column)-first_column[0])*24*60*60

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (C)")
plt.plot(elapsed_time, fourth_column, 'o' ,color="blue")

# plt.savefig("Images/test.png")


# Read the 0th column (time) and the 4th column (Pressure)
time, pressure = pp.get_data_by_time(
      path="Data/TestingPressure_20190418.xls", columns=[0, 1], start_date="Test",
      start_time="0.756646216", end_time="0.765037785")

elapsed_time = (np.array(time)-time[0])*24

plt.xlabel("Time (hours)")
plt.ylabel("Pressure (kPAs)")
plt.plot(time, pressure, color="blue")

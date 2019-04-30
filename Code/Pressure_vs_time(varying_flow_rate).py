import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingPressure_vs_FlowRate_20190423.xls", delimiter = "\t")
data = pp.remove_notes(data)
#
print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
time = data.iloc[:, 0]
time = pd.to_numeric(time)
elapsed_time = (np.array(time)-time[1])*24*60
pressure = data.iloc[:, 1]
pressure = pd.to_numeric(pressure)

plt.title('Pressure Difference vs. Time')
plt.scatter(elapsed_time, pressure, s=1)
#plt.plot(elapsed_time, pressure, '*c', 'MarkerSize', 1)
plt.xlabel('Time (Mins)')
plt.ylabel('Pressure (cm)')

plt.savefig("Images/pressurevtime_20190423.png")

import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingTemperatureDifference_Trial03_20190319.xls", delimiter = "\t")
data = pp.remove_notes(data)
#
print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
time = data.iloc[:, 0]
time = pd.to_numeric(time)
elapsed_time = (np.array(time)-time[0])*24*60
temperatureIn = data.iloc[:, 3]
temperatureIn = pd.to_numeric(temperatureIn)
temperatureOut = data.iloc[:, 2]
temperatureOut = pd.to_numeric(temperatureOut)

In, = plt.plot(elapsed_time, temperatureIn, 'o', color="blue")
Out, = plt.plot(elapsed_time, temperatureOut, 'o', color="green")
plt.title('Temperature vs. Time')
plt.xlabel('Time (Mins)')
plt.ylabel('Temperature (C)')
plt.legend((In, Out), ("Temp. Influent", "Temp. Effluent"))

plt.savefig("Images/temperaturevtime_20190319trial3.png")

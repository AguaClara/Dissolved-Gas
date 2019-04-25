import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingTemperatureDifference_Trial03_20190319.xls", delimiter = "\t")
data = pp.remove_notes(data)
#
print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
time = data.iloc[:,0]
time = pd.to_numeric(time)
temperatureIn = data.iloc[:,3]
temperatureIn = pd.to_numeric(temperatureIn)
temperatureOut = data.iloc[:,2]
temperatureOut = pd.to_numeric(temperatureOut)
elapsed_time = (np.array(time)-time[0])*24

# ax1 is the axis handle for the first y-axis
fig, ax1 = plt.subplots()
ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature In (C)")
# line1 is the line handle for the effluent_turbidity graph
line1, = ax1.plot(elapsed_time, temperatureIn,"o" ,color="blue")

# ax2 is an axis handle for the second y-axis, with the same x-axis as ax1
ax2 = ax1.twinx()
ax2.set_ylabel("Temperature Out (C)")
# line1 is the line handle for the effluent_turbidity graph
line2, = ax2.plot(elapsed_time, temperatureOut,"o", color="green")

plt.legend((line1, line2), ("Temp In", "Temp out"))

# plt.savefig("Images/test.png")

import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingDO_ColdWater_Trial01_20190412.xls", delimiter = "\t")
data = pp.remove_notes(data)
#
print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
time = data.iloc[:, 0]
time = pd.to_numeric(time)
elapsed_time = (np.array(time)-time[0])*24
DOeffluent = data.iloc[:, 5]
DOeffluent = pd.to_numeric(DOeffluent)
DOinffluent = data.iloc[:, 4]
DOinffluent = pd.to_numeric(DOinffluent)

In = plt.plot(elapsed_time, DOinffluent, 'o', color="blue")
Out = plt.plot(elapsed_time, DOeffluent, 'o', color="green")
plt.xlabel('Time (Hour)')
plt.ylabel('Dissolved Oxygen (mg/L)')
plt.legend((In, Out), ("DO In", "DO Out"))












# Bruh the code below is useless
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

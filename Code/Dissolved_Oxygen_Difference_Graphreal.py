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
elapsed_time = (np.array(time)-time[0])*24*60
DOeffluent = data.iloc[:, 5]
DOeffluent = pd.to_numeric(DOeffluent)
DOinffluent = data.iloc[:, 4]
DOinffluent = pd.to_numeric(DOinffluent)

In = plt.scatter(elapsed_time, DOinffluent, s=1)
Out = plt.scatter(elapsed_time, DOeffluent, s=1)
plt.title('Dissolved Oxygen Concentration vs. Time')
plt.xlabel('Time (Mins)')
plt.ylabel('Dissolved Oxygen (mg/L)')
plt.legend((In, Out), ("DO Influent", "DO Effluent"))

plt.savefig("Images/DOconcentrationvtime_20190412.png")

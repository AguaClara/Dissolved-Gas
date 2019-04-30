import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("Data/TestingDOContent_20190423.xls", delimiter = "\t")
data = pp.remove_notes(data)
#
print(data)          # Run this to see the table of data
print(data.columns)  # Run this to see the column labels
time = data.iloc[:, 0]
time = pd.to_numeric(time)
elapsed_time = (np.array(time)-time[1])*24*60
DOinffluenteffluent = data.iloc[:, 4]
DOinffluenteffluent = pd.to_numeric(DOinffluenteffluent)
plt.title('DO Concentration with 1 DO Probe vs. Time')
plt.scatter(elapsed_time, DOinffluenteffluent, 1)
plt.xlabel('Time (Mins)')
plt.ylabel('Dissolved Oxygen (mg/L)')

plt.savefig("Images/DOconcentrationvtime_20190423.png")

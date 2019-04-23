import pandas as pd
import scipy.stats as stats
import aguaclara.research.procoda_parser as pp
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt

data_raw = pd.read_csv("Data/TestingTemperatureDifference_Trial01_20190319.xls", delimiter = "\t")
data = pp.remove_notes(data_raw)

time = data.iloc[:,0]
time = pd.to_numeric(time)
temperatureIn = data.iloc[:,3]
temperatureIn = pd.to_numeric(temperatureIn)
temperature = data.iloc[:,2]
temperatureOut = pd.to_numeric(temperature)

linreg = stats.linregress(time, temperature)
slope, intercept, r_value = linreg[0:3]

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)
#
# Here's a way to graph the regression line with the data:
x_range = np.arange(temperature.iloc[0], temperature.iloc[-1]+1)

plt.xlabel('Time')
plt.ylabel('Temperature In (C)')
plt.plot(time, temperatureIn-temperatureOut, 'o')
plt.plot(x_range, x_range * slope + intercept)

# ax1 is the axis handle for the first y-axis
fig, ax1 = plt.subplots()
ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature In (C)")
# line1 is the line handle for the effluent_turbidity graph
line1, = ax1.plot(time, temperatureIn,"o" ,color="blue")

# ax2 is an axis handle for the second y-axis, with the same x-axis as ax1
ax2 = ax1.twinx()
ax2.set_ylabel("Temperature Out (C)")
# line1 is the line handle for the effluent_turbidity graph
line2, = ax2.plot(time, temperatureOut,"o", color="green")

plt.legend((line1, line2), ("Temp In", "Temp out"))

# Here's a way to graph the regression line with the data:
import numpy as np
import matplotlib.pyplot as plt
x_range = np.arange(temperature.iloc[0], temperature.iloc[-1]+1)

plt.xlabel('Time')
plt.ylabel('Temperature In (C)')
plt.plot(time, temperature, 'o')
plt.plot(x_range, x_range * slope + intercept)

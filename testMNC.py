import pandas as pd
import scipy.stats as stats
import aguaclara.research.procoda_parser as pp

data_raw = pd.read_csv("Data/TestingTemperatureDifference_Trial01_20190319.xls", delimiter = "\t")
data = pp.remove_notes(data_raw)

time = data.iloc[:,0]
time = pd.to_numeric(time)
temperature = data.iloc[:,3]
temperature = pd.to_numeric(temperature)

linreg = stats.linregress(time, temperature)
slope, intercept, r_value = linreg[0:3]

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

# Here's a way to graph the regression line with the data:
import numpy as np
import matplotlib.pyplot as plt
x_range = np.arange(temperature.iloc[0], temperature.iloc[-1]+1)

plt.xlabel('Time')
plt.ylabel('Temperature In (C)')
plt.plot(time, temperature, 'o')
plt.plot(x_range, x_range * slope + intercept)

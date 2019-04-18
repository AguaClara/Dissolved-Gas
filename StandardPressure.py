import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("Test.xlsx")
print(data)         # Run this to see the table of data
print(data.columns) # Run this to see the column labels

# Read the 0th column (time) and the 4th column (effluent turbidity)
time, effluent_turbidity = pp.get_data_by_time(
      path="data", columns=[0, 4], start_date="Test",
      start_time="0.756646216", end_time="0.765037785")
elapsed_time = (np.array(time)-time[0])*24

plt.xlabel("Time (hours)")
plt.ylabel("Effluent Turbidity (NTU)")
plt.plot(time, effluent_turbidity, color="blue")

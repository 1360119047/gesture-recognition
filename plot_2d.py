from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Read the data from the CSV file
csv_path = "IMU_Angle.csv"  # Update this with the actual path
df = pd.read_csv(csv_path)

# Extract the "Acceleration" value from the file name
type = os.path.splitext(os.path.basename(csv_path))[0].split('_')[-1]


# Extracting X, Y, and Z data from the DataFrame
xdata = df[type + '_X']
ydata = df[type + '_Y']
zdata = df[type + '_Z']

# Create three separate 2D plots for X, Y, and Z
fig, (ax_x, ax_y, ax_z) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Plot X data
ax_x.plot(xdata, label='X', color='red')
ax_z.set_xlabel('Time')
ax_x.set_ylabel(type + ' X')
ax_x.legend()

# Plot Y data
ax_y.plot(ydata, label='Y', color='green')
ax_z.set_xlabel('Time')
ax_y.set_ylabel(type + ' Y')
ax_y.legend()

# Plot Z data
ax_z.plot(zdata, label='Z', color='blue')
ax_z.set_xlabel('Time')
ax_z.set_ylabel(type + ' Z')
ax_z.legend()

# Set a title for the plot
ax_x.set_title("Plot for " + type)

plt.savefig(type + ".png")
plt.show()

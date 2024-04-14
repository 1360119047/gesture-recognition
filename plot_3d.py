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


# Creating a 3D scatter plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

# Set a title for the plot
ax.set_title("3D Scatter Plot for " + type)

# Adding labels to the axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.savefig(type + ".png")

plt.show()
plt.close()
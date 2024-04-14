"""
This file does
1. read and save the Raw file into csv file for IMU DATA 
2. read and save MIC Raw file into wav file
3. plot the IMU and MIC data

output folder: xiaochun_data_4_11_22_2023/IMU/CSV_in_1
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import struct
import csv
import pandas as pd

def plot2d (csv_path,PLOT2_folder_path):
    # Read the data from the CSV file
    df = pd.read_csv(csv_path)

    # Extract the "Acceleration" value from the file name
    name = os.path.splitext(os.path.basename(csv_path))[0]
    
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
    ax_x.set_title("Plot for " + name)

    plt.savefig(os.path.join(PLOT2_folder_path, name + ".png") )
    plt.close()

def save_csv(file_path,trial,CSV_folder_path):
    #Tesing open file
    try:
        with open(file_path, 'rb') as file:
            print(f"File '{file_path}' opened successfully.")
    except:   
        print(f"Error: File '{file_path}' not found.")
        return
    
    acc_csv_path = os.path.join(CSV_folder_path, trial + "_Acceleration.csv") 
    gyro_csv_path = os.path.join(CSV_folder_path, trial + "_Gyroscope.csv") 
    angle_csv_path = os.path.join(CSV_folder_path, trial + "_Angle.csv") 
    mag_csv_path = os.path.join(CSV_folder_path, trial + "_Magnetometer.csv") 
    
    with open(file_path, 'rb') as file, \
        open(acc_csv_path, 'w', newline='') as acc_file, \
        open(gyro_csv_path, 'w', newline='') as gyro_file, \
        open(angle_csv_path, 'w', newline='') as angle_file, \
        open(mag_csv_path, 'w', newline='') as mag_file:

        acc_writer = csv.writer(acc_file)
        gyro_writer = csv.writer(gyro_file)
        angle_writer = csv.writer(angle_file)
        mag_writer = csv.writer(mag_file)

        # Write CSV headers for each type of data
        acc_writer.writerow(['Acceleration_X', 'Acceleration_Y', 'Acceleration_Z'])
        gyro_writer.writerow(['Gyroscope_X', 'Gyroscope_Y', 'Gyroscope_Z'])
        angle_writer.writerow(['Angle_X', 'Angle_Y', 'Angle_Z'])
        mag_writer.writerow(['Magnetometer_X', 'Magnetometer_Y', 'Magnetometer_Z'])

        # Read and write IMU data
        while True:
            acc_data = file.read(6)
            if not acc_data:
                break  # End of file

            acc_x, acc_y, acc_z = struct.unpack('<hhh', acc_data)
            acc_writer.writerow([acc_x, acc_y, acc_z])

            gyro_data = file.read(6)
            gyro_x, gyro_y, gyro_z = struct.unpack('<hhh', gyro_data)
            gyro_writer.writerow([gyro_x, gyro_y, gyro_z])

            angle_data = file.read(6)
            angle_x, angle_y, angle_z = struct.unpack('<hhh', angle_data)
            angle_writer.writerow([angle_x, angle_y, angle_z])

            mag_data = file.read(6)
            mag_x, mag_y, mag_z = struct.unpack('<hhh', mag_data)
            mag_writer.writerow([mag_x, mag_y, mag_z])



def draw_spectrogram(filepath,trial,PLOT_folder_path,WAV_folder_path):
    data = np.fromfile(filepath, dtype=np.int16, count=(os.path.getsize(filepath)-11)//2)
    data = data[:len(data)//1024 * 1024].reshape(-1, 4, 256)
    data = np.transpose(data, [1,0,2]).reshape(4,-1)

    # save plt
    for i in range(4): 
        wav_name = trial + "voice%d.wav" % i
        wavfile.write(os.path.join(WAV_folder_path, wav_name), 44100, data[i])
        
        plt.figure()
        # add tile
        plt.title(trial + "voice%d" % i)
        plt.plot(data[i])
        plt_name = trial + 'voice%d.png' % i 
        plt.savefig(os.path.join(PLOT_folder_path, plt_name))
        plt.close()
        
        

# # *** Create folders ***
# # List of folder names
# folder_names = ["ONE", "FIST", "EMOJI", "GUN", "HAND", "BLADE"]

# # Specify the directory where you want to create the folders
# base_directory = os.getcwd()  # Replace with your actual directory path

# # Create folders
# for folder_name in folder_names:
#     folder_path = os.path.join(base_directory, folder_name)
#     os.makedirs(folder_path, exist_ok=True)
#     print(f"Folder '{folder_name}' created at: {folder_path}")
    
# # *** Create folders ***

data_directory = "xiaochun_data_4_11_22_2023"

# folders = [folder for folder in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, folder))]

MIC_folder_path = os.path.join(data_directory, "MIC")
os.makedirs(MIC_folder_path, exist_ok=True)
PLOT_folder_path = os.path.join(MIC_folder_path, "PLOT")
os.makedirs(PLOT_folder_path, exist_ok=True)
WAV_folder_path = os.path.join(MIC_folder_path, "WAV")
os.makedirs(WAV_folder_path, exist_ok=True)

IMU_folder_path = os.path.join(data_directory, "IMU")
os.makedirs(IMU_folder_path, exist_ok=True)
CSV_folder_path = os.path.join(IMU_folder_path, "CSV")
os.makedirs(CSV_folder_path, exist_ok=True)
PLOT2_folder_path = os.path.join(IMU_folder_path, "PLOT")
os.makedirs(PLOT2_folder_path, exist_ok=True)


# *** read data folders/ get spectrogram, recording cvs   ***
for folder in os.listdir(data_directory):
    # open folder
    if os.path.isdir(os.path.join(data_directory, folder)) & ("trial" in folder):
        print(folder)
        # find MIC.RAW and IMU
        trial_folder_path = os.path.join(data_directory, folder)
        for file in os.listdir(trial_folder_path):
            filepath = os.path.join(data_directory, folder, file)
            if "MIC" in file:
                print(file)
                draw_spectrogram(filepath,folder,PLOT_folder_path,WAV_folder_path)
            if "IMU" in file:
                print(file)
                save_csv(filepath,folder,CSV_folder_path)


# *** plot imu csv  ***

for file in os.listdir(CSV_folder_path):
    filepath = os.path.join(CSV_folder_path, file)
    plot2d(filepath,PLOT2_folder_path)
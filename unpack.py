import struct
import csv
import os
import sys

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def unpack_imu_data(file_path):
    #Tesing open file
    try:
        with open(file_path, 'rb') as file:
            print(f"File '{file_path}' opened successfully.")
    except:   
        print(f"Error: File '{file_path}' not found.")
        return

    # **************get the name************* 
    # Extract the base name (file name without directory)
    file_name = os.path.basename(file_path)
    # Remove the file extension (.bin)
    csv_name = os.path.splitext(file_name)[0]
    # **************get the name************* 
    
    
    acc_csv_path = csv_name + "_Acceleration.csv"
    gyro_csv_path = csv_name + "_Gyroscope.csv"
    angle_csv_path = csv_name + "_Angle.csv"
    mag_csv_path = csv_name + "_Magnetometer.csv"
    
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

            
            


if __name__ == "__main__":
    
    # file_path = "data/trial_0_IMU.bin"  # path for testing
    file_path = "IMU.RAW"  # path for testing
    # file_path = "imu.bin" 
    print(os.getcwd())
    unpack_imu_data(file_path)

    
    

    
    
    
    

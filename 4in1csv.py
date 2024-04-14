import os
import numpy as np
import csv
import struct

def save_combined_csv(file_path, trial, CSV_folder_path):
    # Testing open file
    try:
        with open(file_path, 'rb') as file:
            print(f"File '{file_path}' opened successfully.")
    except:
        print(f"Error: File '{file_path}' not found.")
        return

    combined_csv_path = os.path.join(CSV_folder_path, trial + "_Combined.csv")

    with open(file_path, 'rb') as file, open(combined_csv_path, 'w', newline='') as combined_file:
        combined_writer = csv.writer(combined_file)

        # Write CSV headers for all data
        combined_writer.writerow(['Acceleration_X', 'Acceleration_Y', 'Acceleration_Z',
                                  'Gyroscope_X', 'Gyroscope_Y', 'Gyroscope_Z',
                                  'Angle_X', 'Angle_Y', 'Angle_Z',
                                  'Magnetometer_X', 'Magnetometer_Y', 'Magnetometer_Z'])

        # Read and write IMU data
        while True:
            acc_data = file.read(6)
            if not acc_data:
                break  # End of file

            acc_x, acc_y, acc_z = struct.unpack('<hhh', acc_data)

            gyro_data = file.read(6)
            gyro_x, gyro_y, gyro_z = struct.unpack('<hhh', gyro_data)

            angle_data = file.read(6)
            angle_x, angle_y, angle_z = struct.unpack('<hhh', angle_data)

            mag_data = file.read(6)
            mag_x, mag_y, mag_z = struct.unpack('<hhh', mag_data)

            # Write all data to the combined CSV file
            combined_writer.writerow([acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, angle_x, angle_y, angle_z, mag_x, mag_y, mag_z])


# Rest of your code remains unchanged
data_directory = "xiaochun_data_4_11_22_2023"

IMU_folder_path = os.path.join(data_directory, "IMU")
CSV_folder_path = os.path.join(IMU_folder_path, "CSV_in_1")
os.makedirs(CSV_folder_path, exist_ok=True)

# *** read data folders/ get spectrogram, recording cvs   ***
for folder in os.listdir(data_directory):
    if os.path.isdir(os.path.join(data_directory, folder)) and ("trial" in folder):
        print(folder)
        trial_folder_path = os.path.join(data_directory, folder)
        for file in os.listdir(trial_folder_path):
            filepath = os.path.join(data_directory, folder, file)
            if "IMU" in file:
                print(file)
                save_combined_csv(filepath, folder, CSV_folder_path)

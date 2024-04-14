import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from datetime import datetime
import pandas as pd


def get_mic_csv(filepath,trial_folder,save_data_directory):
    # get trial number
    trial_number = trial_folder.split("_")[-1]
    output_folder = os.path.join(save_data_directory, "T" + trial_number)  # Create an output folder named after the trial
    os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
    
    data = np.fromfile(filepath, dtype=np.int16, count=(os.path.getsize(filepath)-11)//2)
    data = data[:len(data)//1024 * 1024].reshape(-1, 4, 256)
    data = np.transpose(data, [1,0,2]).reshape(4,-1)
    
    # print audio_0 to csv file 
    
    
    # output_file_path = os.path.join(output_folder, "audio_0_copy.csv") 
    # np.savetxt(output_file_path, data[0], delimiter=",")

    # print audio_2 to csv file 
    output_file_path2 = os.path.join(output_folder, "audio_2.csv") 
    np.savetxt(output_file_path2, data[2], delimiter=",", fmt='%.2f')




data_directory = "xiaochun_data_4_11_22_2023"

# folders = [folder for folder in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, folder))]

save_data_directory = r"xiaochun_data_4_11_22_2023\dataset\audio_csv"

# *** read data folders/ get spectrogram, recording cvs   ***
for trial_folder in os.listdir(data_directory):
    # open data folder
    if os.path.isdir(os.path.join(data_directory, trial_folder)):
        print(trial_folder)
        # find MIC.RAW and IMU
        trial_folder_path = os.path.join(data_directory, trial_folder)
        for file in os.listdir(trial_folder_path):
            filepath = os.path.join(data_directory, trial_folder, file)
            if "MIC" in file:
                print(file)
                get_mic_csv(filepath,trial_folder,save_data_directory)



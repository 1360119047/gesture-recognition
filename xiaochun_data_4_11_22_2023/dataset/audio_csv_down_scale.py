import os
import numpy as np
from scipy.io import wavfile
import pandas as pd

def downsacle(input_path, output_trial_folder):
    # Read the entire CSV file into a pandas DataFrame
    df = pd.read_csv(input_path)

    # Calculate the number of rows to keep (1/10 of the total rows)
    rows_to_keep = len(df) // 10

    # Use every 10th row to evenly sample the data
    sampled_df = df.iloc[:rows_to_keep * 10:10]
    
    output_csv_filename = os.path.splitext(os.path.basename(input_path))[0] + "_samled.csv"
    
    sampled_file_path = os.path.join(output_trial_folder, output_csv_filename)
    
    sampled_df.to_csv(sampled_file_path, index=False)
    
    print(f"Done processing and saved '{sampled_file_path}'.")


# Example usage for processing all WAV files in the "audie" folder
input_base_folder = "audio_csv_cut"
output_base_folder = "audio_csv_cut_down_scale_10"
output_base_folder_path = os.path.join(os.getcwd(),output_base_folder)
os.makedirs(output_base_folder_path, exist_ok=True)

for root, dirs, files in os.walk(input_base_folder):
    for file in files:
        if file.lower().endswith(".cvs"):
            input_path = os.path.join(root, file)
            
            trial_folder = os.path.split(root)[-1]
            output_trial_folder = os.path.join(output_base_folder,trial_folder)
            os.makedirs(output_trial_folder, exist_ok=True)
            downsacle(input_path, output_trial_folder)
            
            

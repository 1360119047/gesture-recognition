import csv
from datetime import datetime
import math
import os
import pandas as pd

def extract_and_output_csv(input_csv_path, output_csv_path, start_row, end_row):
    try:
        # Read the CSV file
        df = pd.read_csv(input_csv_path)

        # Extract rows 
        selected_rows = df.iloc[1:10]  # Note: Python uses 0-based indexing, so row 12 corresponds to index 11

        # Write the selected rows to another CSV file
        selected_rows.to_csv(output_csv_path, index=False)
        print(f"File '{output_csv_path}'saved.")

    except FileNotFoundError:
        print(f"Error: File '{input_csv_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



# # Load the audio file
# input_file = 'origin\trial_0voice0.wav'
# audio_clip = AudioFileClip(input_file)
# audio_clip_name = os.path.splitext(os.path.basename(input_file))[0]  # Extract input file name without extension

# Read time ranges from the text file
with open("subtract_data.txt", "r") as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:  # Skip the first line as it's a header
    if line.startswith("recording time reranges for"):
        trial = line.split()[-1][:-1]  # Extract trial name like T0
        
        output_trial_folder = os.path.join("audio_csv_cut", trial)  # Create an output folder named after the trial
        os.makedirs(output_trial_folder, exist_ok=True)  # Create the folder if it doesn't exist
        
        trial_number = trial[1:]
        # Load the audio file
        # audio_csv\T0\audio_0.csv
        input_csv_path1 = 'audio_csv\\' + trial + '\\' + 'audio_0.csv'
        input_csv_path2 ='audio_csv\\' + trial + '\\' + 'audio_2.csv'
        
        
    elif line.startswith("set ")&(trial_number=='0'):
        parts = line.split(": ")
        set_number = int(parts[0].split()[-1])
        start_timestamp, end_timestamp = parts[1].strip().split(" - ")

        # Convert timestamps to seconds
        start_time = datetime.strptime(start_timestamp, "%M:%S.%f").time()
        end_time = datetime.strptime(end_timestamp, "%M:%S.%f").time()

        # Clip the audio between the specified timestamps
        start_seconds = start_time.second + start_time.microsecond / 1e6 + start_time.minute * 60
        end_seconds = end_time.second + end_time.microsecond / 1e6 + end_time.minute * 60

        output_csv_name1 = trial + f"_set{set_number}_audio_0.csv"
        output_csv_path1 = os.path.join(output_trial_folder, output_csv_name1)  # Create an output folder named after the trial
        
        output_csv_name2 = trial + f"_set{set_number}_audio_2.csv"
        output_csv_path2 = os.path.join(output_trial_folder, output_csv_name2)  # Create an output folder named after the trial
        
        # round number, time 44100
        start_row = start_seconds * 44100
        end_row = end_seconds * 44100
        
        # round up/
        start_row = math.ceil(start_row)
        end_row = math.ceil(end_row)
        
        extract_and_output_csv(input_csv_path1, output_csv_path1, start_row, end_row)
        extract_and_output_csv(input_csv_path2, output_csv_path2, start_row, end_row)

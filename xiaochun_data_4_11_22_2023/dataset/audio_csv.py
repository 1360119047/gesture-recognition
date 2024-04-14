import os
import numpy as np
from scipy.io import wavfile

def reverse_wav_to_csv(input_wav_path, output_trial_folder):
    try:
        # Read WAV file
        sample_rate, data = wavfile.read(input_wav_path)

        # Reverse the data
        reversed_data = np.flip(data)

        # Construct the output CSV file path within the same structure
        # Use the WAV file name to construct the output CSV file path within the same structure
        output_csv_filename = os.path.splitext(os.path.basename(input_wav_path))[0] + ".csv"
        output_csv_path = os.path.join(output_trial_folder, output_csv_filename)

        try:
            # Save reversed data to CSV
            np.savetxt(output_csv_path, reversed_data, delimiter=',')
            print(f"Done processing and saved '{output_csv_path}'.")
        except FileNotFoundError:
            print(f"Error: File '{output_csv_path}' not found.")


    except FileNotFoundError:
        print(f"Error: File '{input_wav_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage for processing all WAV files in the "audie" folder
input_base_folder = "audio"
output_base_folder = "audio_csv"
output_base_folder_path = os.path.join(os.getcwd(),output_base_folder)
os.makedirs(output_base_folder_path, exist_ok=True)

for root, dirs, files in os.walk(input_base_folder):
    for file in files:
        if file.lower().endswith(".wav"):
            input_wav_path = os.path.join(root, file)
            
            trial_folder = os.path.split(root)[-1]
            output_trial_folder = os.path.join(output_base_folder,trial_folder)
            os.makedirs(output_trial_folder, exist_ok=True)
            reverse_wav_to_csv(input_wav_path, output_trial_folder)
            
            

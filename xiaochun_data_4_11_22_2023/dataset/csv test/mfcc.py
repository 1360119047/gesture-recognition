import pandas as pd
import librosa
import numpy as np
from sklearn.model_selection import train_test_split

# Load dataset_audio
# dataset_path = 'dataset_audio.csv'  # Replace with the actual path to your dataset
dataset_path = 'csv test\dataset_audio.csv'  # debug
dataset = pd.read_csv(dataset_path)

# Select 'audio0' and 'audio2' columns
columns_to_keep = ['audio0', 'audio2']
audio_columns = dataset[columns_to_keep]

new_columns = []
new_dataset = pd.DataFrame()

# Iterate over the selected audio columns
for column in audio_columns:
    print("Column:", column)
    # Extract the raw audio data from the column

    
    # Iterate over each row of the selected audio columns    
    for Rowindex, raw_audio_str in dataset[column].items():
        print(f"Row {Rowindex}")
        
        
        # # Convert raw audio data string to numpy array
        raw_audio_np = np.fromstring(raw_audio_str, sep=',')
        
        
        # print(len(raw_audio_np))
        # Extract MFCC features
        mfcc_features = librosa.feature.mfcc(y=raw_audio_np, sr=44100, n_mfcc=10)

        print(len(mfcc_features))
        
        mfcc_features_list = mfcc_features.tolist()
        
        print(len(mfcc_features_list))
        print(len(mfcc_features_list[0]))
        
        # mfcc_features_flat = mfcc_features.flatten()
        
        # for i in range(1,len(mfcc_features_list) + 1):
        #     new_columns.append(f"{column}_mfcc_array_{i}")  # Expand the column headers from 1 to len(mfcc_features_list)
        
        # Save the numbers into the new column in new_dataset
        for i, array in enumerate(mfcc_features_list, start=1):
            column_name = f"{column}_mfcc_array_{i}"
            new_dataset.loc[Rowindex, column_name] = str(array).strip("[]")
        
        print(f"MFCC processing for column {column} Row {Rowindex} completed.")
        
    print(f"MFCC processing for column '{column}' completed.")

# Save the result to a new CSV file
result_csv_path2 = 'mfcc_test.csv'  # Specify the path for the new CSV file
new_dataset.to_csv(result_csv_path2, index=False)

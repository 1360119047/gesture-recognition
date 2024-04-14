import pandas as pd
import librosa
import numpy as np

# Load your dataset
# dataset_path = 'mfcc_test.csv'  # Replace with the actual path to your dataset
dataset_path = 'csv test\mfcc_test.csv'  # debug
dataset = pd.read_csv(dataset_path)
# # test for the first column
# dataset = dataset[['Acceleration_X', 'Acceleration_Y']]

new_dataset = pd.DataFrame()


# value = dataset.iloc[1, 2]  # Assuming index is 0-based
# print("type in column 3, row 2:", type(value))

# # Keep only 'audio0' and 'audio2' columns
# columns_to_keep = ['audio0', 'audio2']
# dataset = dataset[columns_to_keep]

# # Remove 'audio0' and 'audio2' columns
# columns_to_drop = ['ID', 'name', 'label']
# dataset = dataset.drop(columns=columns_to_drop)



for column in dataset.columns:
    print("Column:", column)
    # add header to the new_dataset dataframe and exband the header form 1 to 20

    if column != 'audio0_mfcc_array_2':
      continue
    
    for Rowindex, value in dataset[column].items():
        if Rowindex != 40:
            continue
        
        numbers = value.split(',')
        
        # Save the numbers into the new column in new_dataset
        for i, num in enumerate(numbers, start=1):
            if i != 87:
                continue
            column_name = f"{column}_{i}"
            # new_dataset.loc[Rowindex, column_name] = num
        

# Save the result to a new CSV file
result_csv_path2 = 'mfcc_expanded.csv'  # Specify the path for the new CSV file
new_dataset.to_csv(result_csv_path2, index=False)
        
# new_dataset = pd.DataFrame(columns=new_columns)  

# # Save the result to a new CSV file
# result_csv_path = 'dataset2addexpand.csv'  # Specify the path for the new CSV file
# new_dataset.to_csv(result_csv_path, index=False)
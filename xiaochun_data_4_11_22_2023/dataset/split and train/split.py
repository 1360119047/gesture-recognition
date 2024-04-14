import pandas as pd

# Load your dataset
dataset_path = 'dataset_audio_only_split.csv' 
# dataset_path = 'csv test/dataset_audio_only_split.csv'  # debug
dataset = pd.read_csv(dataset_path)

# Extract trial index from the 'name' column
dataset['trial_index'] = dataset['name'].str.extract(r'T(\d+)_set').astype(int)

# Group the dataset by 'trial_index' and select one random sample from each group
test_dataset = dataset.groupby('trial_index').apply(lambda x: x.sample(n=1))

# Get the indices of the samples selected for the testing dataset
test_indices = test_dataset['ID']

# Filter out the samples selected for testing to create the training dataset
train_dataset = dataset.loc[~dataset.index.isin(test_indices)]

# Save the training and testing sets to new CSV files
train_dataset.to_csv('train_dataset_audio_only.csv', index=False)
test_dataset.to_csv('test_dataset_audio_only.csv', index=False)
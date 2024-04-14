import csv
from datetime import datetime
import math
import os


def extract_and_output_csv(input_csv_path, output_csv_path, start_row, end_row):
    try:
        with open(input_csv_path, 'r') as input_file:
            print(f"File '{input_csv_path}' opened successfully.")
            reader = csv.reader(input_file)

            # Read the first row as headers
            headers = next(reader)

            # Create a list to store selected rows
            selected_rows = []

            # Read rows and store them in the list
            for _ in range(start_row):  # Skip rows 0 to start_row
                next(reader)
            for _ in range(start_row, end_row):  # Read rows start_row to end_row
                selected_rows.append(next(reader))

        # Write the selected rows to the output CSV file
        with open(output_csv_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)

            # Write headers
            writer.writerow(headers)

            # Write selected rows
            writer.writerows(selected_rows)

        print(f"Selected rows (from {start_row} to {end_row}) written to '{output_csv_path}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_csv_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Read time ranges from the text file
with open("subtract_data.txt", "r") as file:
    lines = file.readlines()


output_folder = os.path.join(os.getcwd(), "CSV_CUT")  # Create an output folder named after the trial
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
input_folder = os.path.join(os.getcwd(), "CSV_in_1")

# Process each line in the file
for line in lines: 
    if line.startswith("recording time reranges for"):
        trial = line.split()[-1][:-1]  # Extract trial name like T0
        
        output_trial_folder = os.path.join(output_folder, trial)  # Create an output folder named after the trial
        os.makedirs(output_trial_folder, exist_ok=True)  # Create the folder if it doesn't exist
        trial_number = trial[1:]
        
        input_csv_name ='trial_' + trial_number + '_Combined.csv'
        input_csv_path = os.path.join(input_folder, input_csv_name)
        
    elif line.startswith("set "):
        parts = line.split(": ")
        set_number = int(parts[0].split()[-1])
        start_timestamp, end_timestamp = parts[1].strip().split(" - ")

        # Convert timestamps to seconds
        start_time = datetime.strptime(start_timestamp, "%M:%S.%f").time()
        end_time = datetime.strptime(end_timestamp, "%M:%S.%f").time()

        # Clip the audio between the specified timestamps
        start_seconds = start_time.second + start_time.microsecond / 1e6 + start_time.minute * 60
        end_seconds = end_time.second + end_time.microsecond / 1e6 + end_time.minute * 60
        
        
        output_csv_name = trial + f"_set{set_number}_imu.cvs"
        output_csv_path = os.path.join(output_trial_folder, output_csv_name)  # Create an output folder named after the trial
        
        # round number, time 10
        start_seconds *= 10
        end_seconds *= 10
        
        # skip first row/
        start_seconds += 1
        end_seconds += 1
        
        # round up/
        start_seconds = math.ceil(start_seconds)
        end_seconds = math.ceil(end_seconds)
        
        extract_and_output_csv(input_csv_path, output_csv_path, start_seconds, end_seconds)
        
        
        
        
        





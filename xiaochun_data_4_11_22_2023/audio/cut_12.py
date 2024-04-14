from moviepy.editor import AudioFileClip
from datetime import datetime
import os

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
        output_folder = os.path.join(os.getcwd(), trial)  # Create an output folder named after the trial
        os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
        
        trial_number = trial[1:]
        # Load the audio file
        input_file = 'origin\\' + 'trial_' + trial_number + 'voice0.wav'
        input_file2 ='origin\\' + 'trial_' + trial_number + 'voice2.wav'
        
        
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

        # Save the clipped audio to a new file
        audio_clip = AudioFileClip(input_file)
        clipped_audio = audio_clip.subclip(start_seconds, end_seconds)
        output_path = os.path.join(output_folder, trial + f"_set{set_number}_audio_0.wav")
        clipped_audio.write_audiofile(output_path, codec="pcm_s16le", fps=44100)

        # Save the clipped audio to a new file
        audio_clip = AudioFileClip(input_file2)
        clipped_audio = audio_clip.subclip(start_seconds, end_seconds)
        output_path = os.path.join(output_folder, trial + f"_set{set_number}_audio_2.wav")
        clipped_audio.write_audiofile(output_path, codec="pcm_s16le", fps=44100)

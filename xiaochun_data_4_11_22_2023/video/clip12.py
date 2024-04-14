from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import timedelta
import os

input_file = 'T14.mp4'
# Generate the output file name based on input file name and segment number
input_file_name = os.path.splitext(os.path.basename(input_file))[0]  # Extract input file name without extension
output_directory = input_file_name + '/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Time_stamp = '00:32'
# time_interval = 10  # Time interval in seconds

# # Convert the start time to timedelta
# start_time = timedelta(minutes=int(Time_stamp[:2]), seconds=int(Time_stamp[-2:])) 


time_interval = 10  # Time interval in seconds
# Convert the start time to timedelt
start_time = timedelta(seconds=26.20)

for i in range(1, 13):  # Loop for 12 segments
    # Calculate start and end times for each segment
    segment_start = start_time + (i - 1) * timedelta(seconds=time_interval)
    # segment_end = segment_start + timedelta(seconds=2)

    # Create a VideoFileClip for the segment
    clip = VideoFileClip(input_file).subclip((segment_start - timedelta(seconds=1)).total_seconds(), (segment_start + timedelta(seconds=1)).total_seconds())


    output_file = os.path.join(output_directory, f'{input_file_name}_{i:02d}.mp4')  # Use segment number with leading zeros

    # Write the segment to a file
    clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

print("Clipping complete.")

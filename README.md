the repo is incomple. you can find how it look like in 
The goal of this project is to use data collect by MIC and IMU data to do reconization, you can find more info here
https://docs.google.com/presentation/d/1lcTPnxFe2JT8OKlVd3GqUNlWWhBYevT8/edit?usp=sharing&ouid=109552043465733562677&rtpof=true&sd=true

I did 15 recordings, and each recording consists of 12 sets of transitions to the gesture. 

Additionally, I had a video for each recording. 

The data at the beginning comprises 15*2 RAW files. First, 

I extracted the data and created CSV, PLOT, and audio files for all of them. 

Since all 12 sets of transitions of the gesture are within one recordingthe, 

I extracted each different set of data into separate CSV files for different recording 

and extracted each different set segmant of video for ground truth. 

I reformatted the IMU CSV files, 

performed MFCC on the MIC data, 


reformatted the MIC CSV files, 

combined both, and reformatted them for training. 

Then, I trained the SVM model.

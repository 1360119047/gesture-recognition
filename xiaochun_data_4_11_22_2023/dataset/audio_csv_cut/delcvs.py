import os
target_directory = os.getcwd()
print(f"Target directory: {target_directory}")
for root, dirs, files in os.walk(target_directory):
        for file in files:
            if file.lower().endswith(".cvs"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
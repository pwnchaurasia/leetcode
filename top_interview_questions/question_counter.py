import os

# Specify the directory path you want to count files in
directory_path = "./75_hard"

# Initialize a dictionary to store folder names and their respective file counts
folder_counts = {}

# Walk through the directory and count files in each folder
for root, dirs, files in os.walk(directory_path):
    # Calculate the count of files in the current folder
    file_count = len(files)

    # Store the folder name and file count in the dictionary
    folder_name = os.path.basename(root)
    folder_counts[folder_name] = file_count

# Display the folder names and their respective file counts
total_sum = 0
for folder, count in folder_counts.items():
    print(f"Folder: {folder}, File Count: {count}")
    total_sum +=count
print(f"Total sum {total_sum}")
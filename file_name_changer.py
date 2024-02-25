import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def rename_file(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)

    # Replace spaces with underscores and add '.py' extension
    new_name = '_'.join(name.split(" ")) + ext

    print("ne", new_name.split(" "))
    new_name = "_".join(i.replace(".", "") for i in  new_name.split(" ")) + ".py"
    print("nnnnnnn", new_name)
    # Get the directory of the file
    directory = os.path.dirname(file_path)

    # Create the new file path
    new_path = os.path.join(directory, new_name)

    # Rename the file
    shutil.move(file_path, new_path)
    print(f'Renamed file: {base_name} to {new_name}')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        created_time = os.path.getctime(file_path)
        current_time = time.time()

        # Check if the file was created within the last 1 minute
        if current_time - created_time < 60:
            rename_file(file_path)

def main():
    folder_to_watch = '/Users/apple/workspace/python/leetcode'  # Replace with the path to your folder

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()

import os
import shutil

# Path of the sorting folder
sorting_folder = r"Path\To\Your\Folder"
os.chdir(sorting_folder)
path = os.getcwd()

file_list = os.listdir(path)

for file_ in file_list:
    try:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]

        if ext == '':
            continue

        dest_folder = os.path.join(path, ext)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        dest_file_path = os.path.join(dest_folder, file_)
        if not os.path.exists(dest_file_path):
            shutil.move(os.path.join(path, file_), dest_file_path)
    
    except PermissionError:
        continue

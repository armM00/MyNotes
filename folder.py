import os

"""
At first run checks if the directory 'D:\Program Files (x86)\HS Softworks\My Notes' exists.
If it doesn't, the script creates a folder by path and a Notes.txt file where it keeps all of the notes.

"""
parent_dir = r"D:\Program Files (x86)"
new_folder = "HS Softworks"
sub_folder = "My Notes"
file_name = "Notes.txt"

folder_path = os.path.join(parent_dir, new_folder, sub_folder)
file_path = os.path.join(folder_path, file_name)


def folder_check():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        exit()
    else:
        pass


def file_check():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
            exit()
    else:
        pass

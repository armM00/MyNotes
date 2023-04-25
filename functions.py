"""
This script is responsible for writing, updating and keeping the notes in 'Notes.txt' file.
"""


FILEPATH = "D:\\Program Files (x86)\\HS Softworks\\My Notes\\Notes.txt"


def get_notes(filepath=FILEPATH):
    with open(filepath, 'r') as custom_file:
        todos_custom = custom_file.readlines()
        return todos_custom


def write_notes(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

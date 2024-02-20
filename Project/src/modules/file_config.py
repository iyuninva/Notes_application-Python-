from modules.programm_config import *
from modules.notes_data import *
from modules.file_config import *

def add_notes():
    try:
        new_note = Notes()
        print("- Enter the name of the note")
        new_note.set_title(text_input())
        print("- Enter text note")
        new_note.set_body(text_input())
        new_file = open(new_note.get_id() + "_" + new_note.get_title() + ".cvs", "w+")
        new_file.write(new_note.display_info())
        new_file.close
        print("- The file was created successfully")
    except (FileExistsError):
        print("\nERROR: file creation error\n")


def edit_notes():
    try:
        None
    except (FileExistsError):
        print("\nERROR: file not found\n")


# def read_list_notes():
#     try:
#         read_file = open(new_note.get_id() + "_" + new_note.get_title() + ".cvs", "r")
#     except (FileExistsError):
#         print("\nERROR: file not found\n")


def delete_notes():
    try:
        None
    except (FileExistsError):
        print("\nERROR: file not found\n")

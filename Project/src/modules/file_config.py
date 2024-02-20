import os
from modules.programm_config import *
from modules.notes_data import *
from modules.file_config import *

note = Notes()


def data_id_notes():
    note.set_id("_2-")
    return note


def data_title_notes():
    print("- Enter the name of the note")
    note.set_title(text_input())
    return note


def data_body_notes():
    print("- Enter text note")
    note.set_body(text_input())
    return note


def add_notes():
    try:
        new_file = open(data_id_notes().get_id() + "_" +
                        data_title_notes().get_title() + ".cvs", "w")
        data_body_notes().get_body()
        new_file.write(note.display_info())
        print("- The file was created successfully")
    except (FileExistsError):
        print("\nERROR: file creation error\n")
    finally:
        new_file.close()


def edit_notes():
    try:
        None
    except (FileNotFoundError):
        print("\nERROR: file not found\n")


def read_list_notes():
    try:
        read_file = open(data_id_notes().get_id() + "_" +
                         data_title_notes().get_title() + ".cvs", "r")
        print(read_file.read())
    except (FileNotFoundError):
        print("\nERROR: file not found\n")
    finally:
        read_file.close()


def delete_notes():
    try:
        os.remove(data_id_notes().get_id() + "_" +
                  data_title_notes().get_title() + ".cvs")
        print("- The file deleted")
    except (FileNotFoundError):
        print("\nERROR: file not found\n")

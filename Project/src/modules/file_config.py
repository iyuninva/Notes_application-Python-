import os
from modules.programm_config import *
from modules.notes_data import *
from modules.file_config import *
from modules.data_search import *


note = Notes()


def data_new_id_notes():
    id = str(id_list())
    note.set_id(id)
    return note


def data_id_notes():
    print("\n- Enter the id of the note")
    note.set_id(text_input())
    return note


def data_title_notes():
    print("\n- Enter the name of the note")
    note.set_title(text_input())
    return note


def data_body_notes():
    print("\n- Enter text note")
    note.set_body(text_input())
    return note


def add_notes():
    try:
        new_file = open(data_new_id_notes().get_id() + "_" +
                        data_title_notes().get_title() + ".cvs", "w")
        data_body_notes().get_body()
        new_file.write(note.display_info())
        print("\n- The file was created successfully\n")
    except (FileExistsError):
        print("\nERROR: file creation error\n")
    finally:
        new_file.close()


def edit_notes():
    try:
        id = data_id_notes().get_id()
        id_file = open(title_note_list(id), "w")
        data_body_notes().get_body()
        id_file.write(note.display_info())
    except (FileNotFoundError):
        print("\nERROR: file not found\n")
    finally:
        id_file.close()


def read_list_notes():
    try:
        id = data_id_notes().get_id()
        read_file = open(title_note_list(id), "r")
        print(read_file.read() + "\n")
    except (FileNotFoundError):
        print("\nERROR: file not found\n")
    finally:
        read_file.close()


def delete_notes():
    try:
        id = data_id_notes().get_id()
        os.remove(title_note_list(id))
        print("\n- The file deleted\n")
    except (FileNotFoundError):
        print("\nERROR: file not found\n")


def sorted_list_notes():
    dict_notes = dict({})
    try:
        for i in os.listdir():
            if i.endswith(".cvs"):
                read_file = open(i, "r")
                dict_notes[i[0]] = read_file.read(19)
                sorted_notes = sorted(dict_notes.items(), key=lambda x: x[1])
        print("\n", sorted_notes, "\n")
    except (Exception):
        print("\nERROR: sorted file\n")
    finally:
        read_file.close()

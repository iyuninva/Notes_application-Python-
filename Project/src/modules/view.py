from modules.programm_config import *
from modules.file_config import *


def start_page():
    print("--- Welcome ---")
    print(" 1. ADD\n 2. EDIT\n 3. READ LIST\n 4. DELETE\n 5. EXIT")
    viewing_case()


def viewing_case():
    try:
        match command_input():
            case 1:
                add_notes()
            case 2:
                print("2")
            case 3:
                read_list_notes()
            case 4:
                delete_notes()
            case 5:
                print("--- EXIT programm ---")
                exit()
    except Exception:
        print("\nERROR: input number command\n")

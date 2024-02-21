from modules.programm_config import *
from modules.file_config import *


def start_page():
    print("--- Welcome ---\n")
    print(" 1. ADD\n 2. EDIT\n 3. READ LIST\n 4. DELETE\n 5. SORTED LIST\n 6. EXIT")
    viewing_case()


def viewing_case():
    try:
        match command_input():
            case 1:
                add_notes()
                start_page()
            case 2:
                edit_notes()
                start_page()
            case 3:
                read_list_notes()
                start_page()
            case 4:
                delete_notes()
                start_page()
            case 5:
                sorted_list_notes()
                start_page()
            case 6:
                print("\n--- EXIT programm ---\n")
                exit()
    except Exception:
        print("\nERROR: input number command\n")
        viewing_case()

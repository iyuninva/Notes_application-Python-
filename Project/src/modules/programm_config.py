
def command_input():
    while True:
        try:
            text_command = int(input("The input field: "))
            return text_command
        except ValueError:
            print("\nERROR: ValueError\n")


def text_input():
    while True:
        try:
            text_command = input("The input field: ")
            return text_command
        except ValueError:
            print("\nERROR: ValueError\n")

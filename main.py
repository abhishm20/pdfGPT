from api import ask_file
import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'invoice.pdf'), "rb+") as file_object:
        ask_file(file_object, "What is invoice number?")

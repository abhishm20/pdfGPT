from api import ask_file


if __name__ == "__main__":
    with open("/Users/abhishek/Downloads/invoice.pdf", "rb+", encoding="utf-8") as file_object:
        ask_file(file_object, "What is invoice number?")

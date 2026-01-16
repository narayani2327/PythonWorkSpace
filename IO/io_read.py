"""IO read"""


def read_file():
    """
    Read and display the contents of a file.
    """
    with open("data.txt", "r", encoding="utf-8") as file_handle:
        content = file_handle.read()
        print(content)


if __name__ == "__main__":
    read_file()

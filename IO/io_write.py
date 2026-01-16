"""IO write"""


# file = open("data.txt","w")
# file.write("Hello file")
# file.close()

# with open("data.txt","a") as file:
#     file.write("Hello testing values")


def write_to_file():
    """
    Write and append text to a file.
    """
    with open("data.txt", "w", encoding="utf-8") as file_handle:
        file_handle.write("Hello file\n")

    with open("data.txt", "a", encoding="utf-8") as file_handle:
        file_handle.write("Hello testing values\n")


if __name__ == "__main__":
    write_to_file()

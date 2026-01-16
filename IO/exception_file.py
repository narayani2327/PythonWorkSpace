"""Exception in files"""


try:
    with open("data.txt", "r", encoding="utf-8") as file_handle:
        content = file_handle.read()
        print(content)
except IOError:
    print("File not found")
finally:
    print("execution completed")

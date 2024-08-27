counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")

def reset_counter():
    counter = 0
    print(f"Local Counter: {counter}")

import os

def print_working_directory():
    print(f"Current working directory: {os.getcwd()}")

def list_files_and_directories():
    files_and_dirs = os.listdir()
    print("Files and directories in current working directory:")
    for item in files_and_dirs:
        print(item)

def create_directory():
    os.mkdir("test_dir")

def change_working_directory():
    os.chdir("test_dir")
    print(f"New working directory: {os.getcwd()}")

def create_file():
    with open("test_file.txt", "w") as f:
        pass

def delete_file_and_directory():
    os.remove("test_file.txt")
    os.rmdir("test_dir")

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    finally:
        print("Division operation completed")

def main():
    for _ in range(3):
        increment_counter()
    reset_counter()
    print_working_directory()
    list_files_and_directories()
    create_directory()
    change_working_directory()
    create_file()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = divide_numbers(a, b)
    if result:
        print(f"Result: {result}")
    delete_file_and_directory()

if __name__ == "__main__":
    main()